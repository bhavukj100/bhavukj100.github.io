#!/usr/bin/env python3
"""Refresh the Airbnb project counts shown on /airbnb/ from Snowflake.

Runs in CI with key-pair authentication. Reads nothing but counts, writes
airbnb/stats.json. If Snowflake is unreachable or the account has lapsed,
the existing stats.json is left untouched so the page keeps showing the
last known good numbers.

Required environment:
  SNOWFLAKE_ACCOUNT        e.g. EVMAFKI-IF65028
  SNOWFLAKE_USER           e.g. BHAVUKJ100
  SNOWFLAKE_ROLE           a read-only role, not ACCOUNTADMIN
  SNOWFLAKE_WAREHOUSE      a warehouse the role may use
  SNOWFLAKE_PRIVATE_KEY    PEM contents of the rsa key registered on the user
  SNOWFLAKE_PRIVATE_KEY_PASSPHRASE  optional, if the key is encrypted
"""

import json
import os
import pathlib
import sys
from datetime import datetime, timezone

OUT = pathlib.Path(__file__).resolve().parent.parent / "airbnb" / "stats.json"

# Read-only. One row out. Nothing here can modify an object.
QUERY = """
select
    count(*)                      as fact_rows,
    count(distinct booking_id)    as unique_bookings,
    count(distinct listing_id)    as unique_listings,
    count(distinct host_id)       as unique_hosts
from airbnb.gold.fact
""".strip()


def fail(message, code=0):
    """Report and leave the committed stats.json alone.

    Exits 0 by default: a lapsed trial account should not turn the
    repository red every night. Pass code=1 to surface a real break.
    """
    print(f"snowflake-stats: {message}", file=sys.stderr)
    sys.exit(code)


def load_private_key():
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import serialization

    pem = os.environ.get("SNOWFLAKE_PRIVATE_KEY", "").strip()
    if not pem:
        fail("SNOWFLAKE_PRIVATE_KEY is not set, leaving stats.json as it is")

    passphrase = os.environ.get("SNOWFLAKE_PRIVATE_KEY_PASSPHRASE") or None
    key = serialization.load_pem_private_key(
        pem.encode(),
        password=passphrase.encode() if passphrase else None,
        backend=default_backend(),
    )
    return key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )


def main():
    for required in ("SNOWFLAKE_ACCOUNT", "SNOWFLAKE_USER"):
        if not os.environ.get(required):
            fail(f"{required} is not set, leaving stats.json as it is")

    try:
        import snowflake.connector
    except ImportError:
        fail("snowflake-connector-python is not installed", code=1)

    try:
        conn = snowflake.connector.connect(
            account=os.environ["SNOWFLAKE_ACCOUNT"],
            user=os.environ["SNOWFLAKE_USER"],
            private_key=load_private_key(),
            role=os.environ.get("SNOWFLAKE_ROLE") or None,
            warehouse=os.environ.get("SNOWFLAKE_WAREHOUSE") or None,
            database="AIRBNB",
            schema="GOLD",
            login_timeout=30,
            network_timeout=60,
        )
    except Exception as exc:  # noqa: BLE001 - any connection problem is the same outcome
        fail(f"could not connect ({type(exc).__name__}), keeping the last known numbers")

    try:
        cur = conn.cursor()
        cur.execute(QUERY)
        row = cur.fetchone()
        if not row:
            fail("query returned no rows, keeping the last known numbers")
        fact_rows, bookings, listings, hosts = (int(v) for v in row[:4])
    except Exception as exc:  # noqa: BLE001
        fail(f"query failed ({type(exc).__name__}), keeping the last known numbers")
    finally:
        try:
            conn.close()
        except Exception:  # noqa: BLE001
            pass

    payload = {
        "fact_rows": fact_rows,
        "unique_bookings": bookings,
        "unique_listings": listings,
        "unique_hosts": hosts,
        "measured_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "AIRBNB.GOLD.FACT",
        "note": "Refreshed by a scheduled GitHub Action running a read-only count against Snowflake.",
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"snowflake-stats: wrote {OUT.name} -> {fact_rows:,} fact rows")


if __name__ == "__main__":
    main()
