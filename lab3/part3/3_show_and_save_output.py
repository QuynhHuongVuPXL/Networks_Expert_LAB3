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

command = "show ip interface brief"

output = net_conn.send_command(command)

output_file = "3_show_ip_int_brief_output.txt"

with open(output_file, "w") as f:
    f.write(output)

print(f"Output saved to {output_file}")

net_conn.disconnect()
