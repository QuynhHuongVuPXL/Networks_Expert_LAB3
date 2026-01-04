#!/usr/bin/env python3


import sys
import hashlib
import requests
from ncclient import manager
from ncclient.operations.rpc import RPCError


# ===== GitHub RAW config (public repo) =====
GITHUB_RAW_URL = (
    "https://raw.githubusercontent.com/"
    "QuynhHuongVuPXL/Networks_Expert_LAB3/"
    "main/lab4/configs/iosxe_config.xml"
)

# ===== Device credentials =====
DEVICE = {
    "host": "192.168.56.101",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!",
}

# ===== NETCONF capabilities we care about =====
CANDIDATE_CAP = "urn:ietf:params:netconf:capability:candidate:1.0"
VALIDATE_CAP_10 = "urn:ietf:params:netconf:capability:validate:1.0"
VALIDATE_CAP_11 = "urn:ietf:params:netconf:capability:validate:1.1"


def fetch_config_from_github(url: str) -> str:
    r = requests.get(url, timeout=20)
    if r.status_code != 200:
        raise RuntimeError(f"GitHub fetch failed: {r.status_code} {r.text[:200]}")

    xml = r.text.strip()

    # NETCONF edit-config payload should start with <config ...>
    if not xml.lstrip().startswith("<config"):
        raise ValueError("Downloaded content is not a NETCONF <config> payload.")

    sha = hashlib.sha256(xml.encode("utf-8")).hexdigest()
    print(f"[OK] Config fetched from GitHub ({len(xml)} bytes) sha256={sha[:12]}...")

    return xml


def has_cap(caps, needle: str) -> bool:
    return any(needle in c for c in caps)


def main() -> int:
    print("1) Fetching config from GitHub (single source of truth)...")
    try:
        config_xml = fetch_config_from_github(GITHUB_RAW_URL)
    except Exception as e:
        print("[FAIL] Could not fetch/validate GitHub XML:", e)
        return 1

    print("2) Connecting to IOS-XE via NETCONF...")
    try:
        with manager.connect(
            host=DEVICE["host"],
            port=DEVICE["port"],
            username=DEVICE["username"],
            password=DEVICE["password"],
            allow_agent=False,
            look_for_keys=False,
            hostkey_verify=False,
            timeout=30,
            device_params={"name": "iosxe"},
        ) as m:

            print("[OK] NETCONF connected")

            caps = list(m.server_capabilities)

            # Hard requirement: candidate datastore
            if not has_cap(caps, CANDIDATE_CAP):
                print("[FAIL] Candidate datastore capability is missing on this device.")
                print(f"       Expected: {CANDIDATE_CAP}")
                print("       Fix on IOS-XE (if supported by your image):")
                print("         conf t")
                print("         netconf-yang")
                print("         netconf-yang feature candidate-datastore")
                print("         end")
                return 1

            validate_supported = has_cap(caps, VALIDATE_CAP_10) or has_cap(caps, VALIDATE_CAP_11)
            print("[OK] candidate datastore supported")
            if validate_supported:
                print("[OK] validate capability supported (optional)")

            locked = False
            try:
                # Atomic staging: lock -> discard -> edit -> (validate) -> commit
                print("3) Locking candidate...")
                m.lock("candidate")
                locked = True
                print("[OK] candidate locked")

                print("4) discard-changes (clean candidate)...")
                m.discard_changes()
                print("[OK] candidate cleared")

                print("5) edit-config -> candidate (single atomic payload)...")
                reply = m.edit_config(
                    target="candidate",
                    config=config_xml,
                    default_operation="merge",
                    error_option="rollback-on-error",
                )
                # If you want to see raw rpc-reply:
                # print(reply.xml)
                print("[OK] staged config in candidate")

                if validate_supported:
                    print("6) validate(candidate)...")
                    m.validate(source="candidate")
                    print("[OK] validate passed")

                print("7) commit candidate -> running...")
                c = m.commit()
                # print(c.xml)
                print("[OK] commit done")

                print("\n[SUCCESS] Full configuration deployed atomically and is now active.")
                return 0

            except RPCError as e:
                print("\n[FAIL] NETCONF RPCError during deployment")
                print("Message:", getattr(e, "message", None))
                print("Path:", getattr(e, "path", None))
                print("Info:", getattr(e, "info", None))

                print("\nRolling back staged changes (discard-changes)...")
                try:
                    m.discard_changes()
                    print("[OK] discard-changes executed")
                except Exception as ee:
                    print("[WARN] discard-changes failed:", ee)

                return 1

            except Exception as e:
                print("\n[FAIL] Unexpected error during deployment:", e)

                print("\nRolling back staged changes (discard-changes)...")
                try:
                    m.discard_changes()
                    print("[OK] discard-changes executed")
                except Exception as ee:
                    print("[WARN] discard-changes failed:", ee)

                return 1

            finally:
                if locked:
                    print("8) Unlocking candidate...")
                    try:
                        m.unlock("candidate")
                        print("[OK] candidate unlocked")
                    except Exception as e:
                        print("[WARN] unlock candidate failed:", e)

    except Exception as e:
        print("[FAIL] NETCONF connection failed:", e)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
