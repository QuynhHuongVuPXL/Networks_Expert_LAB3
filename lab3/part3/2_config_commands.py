from netmiko import ConnectHandler

device = {
    "device_type": "cisco_xe",
    "ip": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
    "secret": "cisco123!",
}

net_conn = ConnectHandler(**device)
net_conn.enable()

config_commands = [
    "interface Loopback10",
    "ip address 10.10.10.1 255.255.255.255",
    "description Created_by_Netmiko",
]

output = net_conn.send_config_set(config_commands)
print(output)

save_output = net_conn.save_config()
print("Configuration saved.")

net_conn.disconnect()
