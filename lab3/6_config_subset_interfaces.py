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

# Use real interfaces from your CSR1000v
interfaces_to_configure = [
    "Loopback70",
    "Loopback71",
    "Loopback72"
]

for intf in interfaces_to_configure:
    commands = [
        f"interface {intf}",
        f"ip address 172.16.{interfaces_to_configure.index(intf)}.1 255.255.255.0",
        "description Configured_by_Python",
        "no shutdown"
    ]
    print(f"\nConfiguring {intf}...")
    output = net_conn.send_config_set(commands)
    print(output)

net_conn.save_config()
net_conn.disconnect()
