from netmiko import ConnectHandler

devices = [
    {
        "device_type": "cisco_xe",
        "ip": "192.168.56.101",    
        "username": "cisco",
        "password": "cisco123!",
        "secret": "cisco123!",
    },
    {
        "device_type": "cisco_xe",
        "ip": "192.168.56.102",   
        "username": "admin",
        "password": "password",
        "secret": "password",
    }
]

command = "show ip interface brief"

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
