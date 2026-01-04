from ncclient import manager
from ncclient.operations.rpc import RPCError
import requests
import sys
import xml.etree.ElementTree as ET

GITHUB_RAW_URL = (
    "https://raw.githubusercontent.com/"
    "QuynhHuongVuPXL/Networks_Expert_LAB3/"
    "main/lab4/configs/iosxe_config.xml"
)

DEVICE = {
    "host": "192.168.56.101",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!",
}

def get_config_from_github(url: str) -> str:
    r = requests.get(url, timeout=20)
    if r.status_code != 200:
        raise RuntimeError(f"GitHub fetch failed: {r.status_code} {r.text[:200]}")
    return r.text.strip()

def ensure_is_netconf_config(xml_text: str) -> str:
    # Validate that root is <config> (NETCONF edit-config payload root)
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        raise RuntimeError(f"XML parse error: {e}")

    if root.tag != "config":
        raise RuntimeError(f"Root element must be <config>, got <{root.tag}>")

    return xml_text

def supports_candidate(caps) -> bool:
    return any("capability:candidate" in c for c in caps)

def supports_validate(caps) -> bool:
    return any("capability:validate" in c for c in caps)

def main():
    print("1) Fetching config from GitHub...")
    full_xml = get_config_from_github(GITHUB_RAW_URL)
    full_xml = ensure_is_netconf_config(full_xml)

    print("2) Connecting to IOS-XE via NETCONF...")
    with manager.connect(
        host=DEVICE["host"],
        port=DEVICE["port"],
        username=DEVICE["username"],
        password=DEVICE["password"],
        hostkey_verify=False,
        look_for_keys=False,
        allow_agent=False,
        device_params={"name": "csr"}  # helps with IOS-XE/CSR quirks
    ) as m:

        caps = list(m.server_capabilities)
        use_candidate = supports_candidate(caps)
        can_validate = supports_validate(caps)

        print("DEBUG candidate supported:", use_candidate)
        print("DEBUG validate supported:", can_validate)

        target = "candidate" if use_candidate else "running"

        # lock for clean atomic transaction
        locked = False
        try:
            if use_candidate:
                print("3) Locking candidate...")
                m.lock("candidate")
                locked = True

            print(f"4) edit-config to {target} (atomic payload: native + ospf)...")
            m.edit_config(
                target=target,
                config=full_xml,
                default_operation="merge",
                error_option="rollback-on-error"
            )

            if use_candidate and can_validate:
                print("5) Validating candidate...")
                m.validate(source="candidate")

            if use_candidate:
                print("6) Commit candidate -> running...")
                m.commit()

            print("SUCCESS: Configuration deployed atomically.")

        except RPCError as e:
            print("NETCONF RPCError")
            print("Message:", getattr(e, "message", ""))
            print("Path:", getattr(e, "path", ""))
            print("Info:", getattr(e, "info", ""))
            if use_candidate:
                print("Discarding candidate changes...")
                try:
                    m.discard_changes()
                except Exception:
                    pass
            sys.exit(1)

        except Exception as e:
            print("Unexpected error:", e)
            if use_candidate:
                print("Discarding candidate changes...")
                try:
                    m.discard_changes()
                except Exception:
                    pass
            sys.exit(1)

        finally:
            if use_candidate and locked:
                print("Unlocking candidate...")
                try:
                    m.unlock("candidate")
                except Exception:
                    pass

    print("Done.")

if __name__ == "__main__":
    main()
