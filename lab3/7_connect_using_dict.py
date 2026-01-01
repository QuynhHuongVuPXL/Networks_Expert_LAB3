from netmiko import ConnectHandler

# Device connection information stored in a Python dictionary
device = {
    "device_type": "cisco_xe",
    "ip": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
    "secret": "cisco123!",
}

# Connect using the dictionary
net_conn = ConnectHandler(**device)
net_conn.enable()

output = net_conn.send_command("show version")
print(output)

net_conn.disconnect()
