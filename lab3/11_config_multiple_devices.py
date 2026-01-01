from netmiko import ConnectHandler

# List of devices
devices = [
    {
        "device_type": "cisco_xe",
        "ip": "192.168.56.101",     # your real CSR1000v
        "username": "cisco",
        "password": "cisco123!",
        "secret": "cisco123!",
    },
    {
        "device_type": "cisco_xe",
        "ip": "192.168.56.102",     # fake device (example)
        "username": "admin",
        "password": "password",
        "secret": "password",
    }
]

# Configuration commands sent to each device
config_commands = [
    "interface Loopback200",
    "ip address 200.200.200.1 255.255.255.255",
    "description Configured_on_multiple_devices",
]

# Loop through devices and send config
for dev in devices:
    print(f"\n----- Connecting to {dev['ip']} -----")

    try:
        net_conn = ConnectHandler(**dev)
        net_conn.enable()

        print("Sending configuration...")
        output = net_conn.send_config_set(config_commands)
        print(output)

        net_conn.save_config()
        print("Configuration saved.")

        net_conn.disconnect()

    except Exception as e:
        print(f"FAILED to configure {dev['ip']} : {e}")
