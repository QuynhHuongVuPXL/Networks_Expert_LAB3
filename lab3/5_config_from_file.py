from netmiko import ConnectHandler

device = {
    "device_type": "cisco_xe",
    "ip": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
    "secret": "cisco123!",
}

# Load configuration commands from external file
with open("5_config_commands.txt", "r") as f:
    config_commands = f.read().splitlines()

net_conn = ConnectHandler(**device)
net_conn.enable()

# Apply configuration
output = net_conn.send_config_set(config_commands)
print(output)

# Save config
net_conn.save_config()

net_conn.disconnect()
