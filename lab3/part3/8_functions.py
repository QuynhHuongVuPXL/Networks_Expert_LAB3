from netmiko import ConnectHandler

device = {
    "device_type": "cisco_xe",
    "ip": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
    "secret": "cisco123!",
}

def connect_device(device_info):
    """Connect to the device and enter enable mode."""
    connection = ConnectHandler(**device_info)
    connection.enable()
    return connection

def send_show(connection, command):
    """Send a show command."""
    return connection.send_command(command)

def send_config(connection, config_list):
    """Send configuration commands."""
    return connection.send_config_set(config_list)

def disconnect_device(connection):
    """Close SSH connection."""
    connection.disconnect()

net_conn = connect_device(device)

print("=== SHOW IP INT BRIEF ===")
output = send_show(net_conn, "show ip interface brief")
print(output)

config_commands = [
    "interface Loopback80",
    "ip address 80.80.80.1 255.255.255.255",
    "description Created_with_Functions"
]

print("\n=== SENDING CONFIG ===")
config_output = send_config(net_conn, config_commands)
print(config_output)

disconnect_device(net_conn)
