import json
import requests

# Disable SSL certificate warnings (lab environment)
requests.packages.urllib3.disable_warnings()

# RESTCONF API URL
api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces"

# HTTP headers for RESTCONF using JSON
headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json"
}

# Basic authentication credentials
basicauth = ("cisco", "cisco123!")

# Send GET request
resp = requests.get(
    api_url,
    auth=basicauth,
    headers=headers,
    verify=False
)

# Print HTTP response code
print(resp)

# Convert JSON response to Python object
response_json = resp.json()

# Pretty-print the JSON output
print(json.dumps(response_json, indent=4))
