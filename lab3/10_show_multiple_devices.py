from netmiko import ConnectHandler

# List of multiple devices
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
        "ip": "192.168.56.102",     # example (fake) router
        "username": "admin",
        "password": "password",
        "secret": "password",
    }
]

# Command to run on each device
command = "show ip interface brief"

# Loop through devices
for dev in devices:
    print(f"\n----- Connecting to {dev['ip']} -----")

    try:
        net_conn = ConnectHandler(**dev)
        net_conn.enable()

        output = net_conn.send_command(command)
        print(output)

        net_conn.disconnect()
    
    except Exception as e:
        print(f"Failed to connect to {dev['ip']} : {e}")
