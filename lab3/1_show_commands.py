from netmiko import ConnectHandler

# device = {
#     "device_type": "cisco_xe",
#     "ip": "192.168.56.101",  
#     "username": "cisco",
#     "password": "cisco123!",
#     "secret": "cisco123!",
# }

device = {
    "device_type": "cisco_ios",
    "ip": "172.16.6.129",
    "username": "student",
    "password": "lab123",
    "secret": "lab123",
}

net_conn = ConnectHandler(**device)
net_conn.enable()

output = net_conn.send_command("show ip interface brief")
print(output)

net_conn.disconnect()
