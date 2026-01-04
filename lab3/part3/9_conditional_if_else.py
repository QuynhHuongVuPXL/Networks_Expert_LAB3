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

desired_hostname = "MY_ROUTER"
output = net_conn.send_command("show running-config | include hostname")
print("Current hostname:", output)

if desired_hostname in output:
    print("\nHostname is already correct. No changes needed.")
else:
    print("\nHostname is incorrect. Fixing it now...")
    print(net_conn.send_config_set([f"hostname {desired_hostname}"]))

    print(net_conn.send_command("write memory", expect_string=r"#"))
    print("Hostname updated and configuration saved.")

net_conn.disconnect()
