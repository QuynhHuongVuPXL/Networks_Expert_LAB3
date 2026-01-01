from netmiko import ConnectHandler
from datetime import datetime

device = {
    "device_type": "cisco_xe",
    "ip": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
    "secret": "cisco123!",
}

net_conn = ConnectHandler(**device)
net_conn.enable()

running_config = net_conn.send_command("show running-config")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_filename = f"backup_{device['ip']}_{timestamp}.cfg"

with open(backup_filename, "w") as backup_file:
    backup_file.write(running_config)

print(f"Backup saved as: {backup_filename}")

net_conn.disconnect()
