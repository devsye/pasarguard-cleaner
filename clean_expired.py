import os
import time
import requests

BASE = os.environ["PANEL_URL"].rstrip("/")


def login():
    s = requests.Session()
    r = s.post(
        f"{BASE}/api/admin/token",
        data={
            "username": os.environ["PANEL_USER"],
            "password": os.environ["PANEL_PASS"],
        },
        timeout=30,
    )
    r.raise_for_status()
    s.headers["Authorization"] = f"Bearer {r.json()['access_token']}"
    return s


s = login()
names = []
for st in ("expired", "limited"):
    offset = 0
    while True:
        r = s.get(
            f"{BASE}/api/users",
            params={"status": st, "limit": 100, "offset": offset},
            timeout=30,
        )
        r.raise_for_status()
        users = r.json().get("users", [])
        names += [u["username"] for u in users]
        if len(users) < 100:
            break
        offset += 100

print(len(names), "users remaining")
if names and input("Delete them? (yes): ") == "yes":
    ok = 0
    for n in names:
        for attempt in range(4):
            try:
                d = s.delete(f"{BASE}/api/user/{n}", timeout=30)
                if d.status_code in (200, 404):
                    ok += 1
                else:
                    print(n, d.status_code, d.text[:80])
                break
            except requests.exceptions.RequestException:
                print("Connection lost, waiting...")
                time.sleep(5 * (attempt + 1))
                try:
                    s = login()
                except Exception:
                    pass
        time.sleep(1)
    print("Deleted:", ok)
