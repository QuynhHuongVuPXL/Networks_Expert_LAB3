from netmiko import ConnectHandler

switch = {
    "device_type": "cisco_ios",
    "ip": "172.16.6.132",        # Switch management IP
    "username": "student",
    "password": "lab123",
    "secret": "lab123",
}

print("Connecting to SWITCH...")

net_conn = ConnectHandler(**switch)
net_conn.enable()

print("\n=== SHOW VLAN BRIEF ===")
print(net_conn.send_command("show vlan brief"))

print("\n=== SHOW INTERFACES TRUNK ===")
print(net_conn.send_command("show interfaces trunk"))

print("\n=== SHOW IP INTERFACE BRIEF ===")
print(net_conn.send_command("show ip interface brief"))

net_conn.disconnect()
print("\nDisconnected from switch.")
