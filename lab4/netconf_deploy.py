from ncclient import manager
import requests
import sys

# -------- GitHub config --------
GITHUB_RAW_URL = "https://raw.githubusercontent.com/QuynhHuongVuPXL/Networks_Expert_LAB3/main/lab4/configs/iosxe_config.xml"

# -------- Device credentials --------
DEVICE = {
    "host": "192.168.56.101",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!"
}

def get_config_from_github(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch config from GitHub")
        sys.exit(1)
    return response.text

def main():
    print("1. Fetching config from GitHub...")
    config_xml = get_config_from_github(GITHUB_RAW_URL)

    print("2. Connecting via NETCONF...")
    with manager.connect(
        host=DEVICE["host"],
        port=DEVICE["port"],
        username=DEVICE["username"],
        password=DEVICE["password"],
        hostkey_verify=False
    ) as m:

        # Check of candidate supported wordt
        use_candidate = any(":candidate" in cap for cap in m.server_capabilities)

        try:
            if use_candidate:
                print("3. Candidate datastore supported")
                m.edit_config(target="candidate", config=config_xml)
                print("4. Committing candidate to running...")
                m.commit()
            else:
                print("3. Candidate NOT supported, using running datastore")
                m.edit_config(target="running", config=config_xml)

            print("5. Deployment successful!")

        except Exception as e:
            print("❌ Error occurred")
            if use_candidate:
                m.discard_changes()
            print(e)


if __name__ == "__main__":
    main()
