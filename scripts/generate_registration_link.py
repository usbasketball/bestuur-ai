#!/usr/bin/env python3
import sys
import os
import time
import hmac
import hashlib
from datetime import datetime
from pathlib import Path


def load_env_file(file_path: Path):
    if not file_path.is_file():
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, val = line.split('=', 1)
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if key not in os.environ:
                    os.environ[key] = val


def main():
    root_dir = Path(__file__).resolve().parent.parent
    load_env_file(root_dir / '.env.local')
    load_env_file(root_dir / '.env')

    secret = os.environ.get('REGISTRATION_SECRET')
    if not secret:
        print('Error: REGISTRATION_SECRET is not set.', file=sys.stderr)
        print('Add it to .env.local or pass it inline:', file=sys.stderr)
        print('  REGISTRATION_SECRET="<your-secret>" python3 scripts/generate_registration_link.py [hours]', file=sys.stderr)
        sys.exit(1)

    hours_valid = 72.0
    if len(sys.argv) > 1:
        try:
            val = float(sys.argv[1])
            if val > 0:
                hours_valid = val
        except ValueError:
            pass

    site_url = os.environ.get('NEXT_PUBLIC_SITE_URL', 'https://usbasketball.nl').rstrip('/')

    now_ts = int(time.time())
    expires = now_ts + int(round(hours_valid * 3600))
    token = hmac.new(secret.encode('utf-8'), str(expires).encode('utf-8'), hashlib.sha256).hexdigest()

    expiry_dt = datetime.fromtimestamp(expires).astimezone()

    print("\n=======================================================")
    print(" US Basketball - Private Registration Link")
    print("=======================================================")
    print(f"Valid duration : {int(hours_valid) if hours_valid.is_integer() else hours_valid} hours")
    print(f"Expires at     : {expiry_dt.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print("-------------------------------------------------------")
    print("Generated link:\n")
    print(f"{site_url}/register?expires={expires}&token={token}")
    print("\n=======================================================\n")


if __name__ == '__main__':
    main()
