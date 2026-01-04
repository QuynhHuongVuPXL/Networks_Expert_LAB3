from ncclient import manager
import xml.dom.minidom

# Connect to CSR1kv via NETCONF
m = manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

# Commented out to avoid 400+ lines
"""
print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    print(capability)
"""

# Get FULL running configuration
netconf_reply = m.get_config(source="running")
print("===== FULL RUNNING CONFIG =====")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# Get ONLY Cisco IOS-XE native YANG model
netconf_filter = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""

netconf_reply = m.get_config(source="running", filter=netconf_filter)
print("===== FILTERED (NATIVE) CONFIG =====")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# Change hostname (edit-config)
netconf_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>CSR1kv</hostname>
  </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_hostname)
print("===== HOSTNAME CHANGE RESULT =====")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# Create Loopback1 interface
netconf_loopback = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>1</name>
        <description>My first NETCONF loopback</description>
        <ip>
          <address>
            <primary>
              <address>10.1.1.1</address>
              <mask>255.255.255.0</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print("===== LOOPBACK1 CREATION RESULT =====")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# Attempt duplicate IP (EXPECTED ERROR)
netconf_newloop = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>2</name>
        <description>My second NETCONF loopback</description>
        <ip>
          <address>
            <primary>
              <address>10.1.1.1</address>
              <mask>255.255.255.0</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

try:
    m.edit_config(target="running", config=netconf_newloop)
except Exception as e:
    print("===== EXPECTED ERROR (DUPLICATE IP) =====")
    print(e)
