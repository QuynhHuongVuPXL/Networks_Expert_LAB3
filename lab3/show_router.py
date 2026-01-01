from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "ip": "172.16.6.129",        # Router VLAN 10 gateway
    "username": "student",
    "password": "lab123",
    "secret": "lab123",
}

print("Connecting to ROUTER...")

net_conn = ConnectHandler(**router)
net_conn.enable()

print("\n=== SHOW IP INTERFACE BRIEF ===")
print(net_conn.send_command("show ip interface brief"))

print("\n=== SHOW IP ROUTE ===")
print(net_conn.send_command("show ip route"))

print("\n=== SHOW VERSION ===")
print(net_conn.send_command("show version"))

net_conn.disconnect()
print("\nDisconnected from router.")
