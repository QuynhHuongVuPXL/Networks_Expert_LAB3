from ncclient import manager
from ncclient.operations.rpc import RPCError
import requests
import sys
import re

# GitHub RAW config 
GITHUB_RAW_URL = (
    "https://raw.githubusercontent.com/"
    "QuynhHuongVuPXL/Networks_Expert_LAB3/"
    "main/lab4/configs/iosxe_config.xml"
)

# Device credentials
DEVICE = {
    "host": "192.168.56.101",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!"
}

# Helpers
def get_config_from_github(url: str) -> str:
    r = requests.get(url, timeout=20)
    if r.status_code != 200:
        print(f"Failed to fetch config from GitHub: {r.status_code}")
        print(r.text[:200])
        sys.exit(1)
    return r.text.strip()

def extract_block(xml: str, tag: str) -> str | None:
    """
    Extracts <tag>...</tag> including namespace attributes
    """
    match = re.search(
        rf"(<{tag}\b[^>]*>.*?</{tag}>)",
        xml,
        flags=re.DOTALL
    )
    return match.group(1) if match else None

def wrap_config(inner_xml: str) -> str:
    return f"<config>{inner_xml}</config>"

# Main logic
def main():
    print("1. Fetching config from GitHub (single source of truth)...")
    full_xml = get_config_from_github(GITHUB_RAW_URL)

    native_block = extract_block(full_xml, "native")
    ospf_block = extract_block(full_xml, "ospf")

    if not native_block:
        print("No <native> block found in GitHub XML")
        sys.exit(1)

    print("2. Connecting to IOS-XE via NETCONF...")
    with manager.connect(
        host=DEVICE["host"],
        port=DEVICE["port"],
        username=DEVICE["username"],
        password=DEVICE["password"],
        hostkey_verify=False
    ) as m:

        caps = list(m.server_capabilities)
        use_candidate = any(":candidate" in cap for cap in caps)
        supports_ospf_model = any("Cisco-IOS-XE-ospf" in cap for cap in caps)

        print("DEBUG candidate supported:", use_candidate)
        print("DEBUG Cisco-IOS-XE-ospf supported:", supports_ospf_model)

        target = "candidate" if use_candidate else "running"

        # Deploy native config
        try:
            print(f"3. Deploying native config (hostname + interfaces) to {target}...")
            m.edit_config(target=target, config=wrap_config(native_block))

            if use_candidate:
                print("4. Committing candidate datastore...")
                m.commit()

            print("Native configuration deployed successfully")

        except RPCError as e:
            print("NETCONF RPCError during native deploy")
            print("Message:", e.message)
            print("Path:", e.path)
            print("Info:", e.info)
            if use_candidate:
                m.discard_changes()
            sys.exit(1)

        except Exception as e:
            print("Unexpected error during native deploy")
            print(e)
            if use_candidate:
                m.discard_changes()
            sys.exit(1)

        # ------------------------------
        # Deploy OSPF (separately)
        # ------------------------------
        if ospf_block:
            if supports_ospf_model:
                print("5. Deploying OSPF configuration separately...")
                try:
                    m.edit_config(
                        target="running",
                        config=wrap_config(ospf_block)
                    )
                    print("OSPF deployed successfully")
                except RPCError as e:
                    print("OSPF deployment failed")
                    print("Reason:", e.info)
                    print("Native config remains active (atomic behavior)")
            else:
                print("Cisco-IOS-XE-ospf YANG model not supported on this IOS-XE image")
        else:
            print("5. No OSPF block found in GitHub XML (skipping)")

    print("\nDeployment finished")

# Entry point
if __name__ == "__main__":
    main()
