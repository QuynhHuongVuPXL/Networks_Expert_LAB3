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

# Desired hostname
desired_hostname = "MY_ROUTER"

# Get current hostname
output = net_conn.send_command("show running-config | include hostname")

print("Current hostname:", output)

# ---- CONDITIONAL LOGIC ----
if desired_hostname in output:
    print("\nHostname is already correct. No changes needed.")
else:
    print("\nHostname is incorrect. Fixing it now...")
    config_cmd = [f"hostname {desired_hostname}"]
    config_output = net_conn.send_config_set(config_cmd)
    print(config_output)
    net_conn.save_config()
    print("Hostname updated and configuration saved.")

# Disconnect
net_conn.disconnect()
