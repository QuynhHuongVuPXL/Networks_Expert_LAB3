from netmiko import ConnectHandler
from datetime import datetime

devices = [
    {
        "device_type": "cisco_xe",
        "ip": "192.168.56.101",
        "username": "cisco",
        "password": "cisco123!",
        "secret": "cisco123!",
    }
]

# =============================
# BASELINE CONFIG REQUIREMENTS
# =============================

baseline = {
    "hostname": "NET-AUTO-ROUTER",
    "ntp_server": "10.10.10.10",
    "aaa_new_model": True,
    "loopback0_ip": "1.1.1.1 255.255.255.255",
    "gi1_description": "Uplink_to_Core",
}

# =============================
# COMPLIANCE CHECK FUNCTIONS
# =============================

def connect_device(device):
    conn = ConnectHandler(**device)
    conn.enable()
    return conn

def check_hostname(conn):
    current = conn.send_command("show run | include hostname")
    return "hostname " + baseline["hostname"] in current

def check_ntp(conn):
    ntp = conn.send_command("show run | include ntp server")
    return baseline["ntp_server"] in ntp

def check_aaa(conn):
    aaa = conn.send_command("show run | include aaa new-model")
    return "aaa new-model" in aaa

def check_loopback0(conn):
    loop = conn.send_command("show run interface loopback0")
    return baseline["loopback0_ip"] in loop

def check_gi1_description(conn):
    desc = conn.send_command("show run interface gi1 | include description")
    return baseline["gi1_description"] in desc

# =============================
# AUTO-FIX FUNCTIONS
# =============================

def fix_hostname(conn):
    conn.send_config_set([f"hostname {baseline['hostname']}"])

def fix_ntp(conn):
    conn.send_config_set([f"ntp server {baseline['ntp_server']}"])

def fix_aaa(conn):
    conn.send_config_set(["aaa new-model"])

def fix_loopback0(conn):
    conn.send_config_set([
        "interface Loopback0",
        f"ip address {baseline['loopback0_ip']}",
    ])

def fix_gi1_description(conn):
    conn.send_config_set([
        "interface GigabitEthernet1",
        f"description {baseline['gi1_description']}",
    ])

# =============================
# MAIN AUTOMATION LOGIC
# =============================

report = []
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

report.append(f"NETWORK COMPLIANCE REPORT - {timestamp}")
report.append("=" * 60 + "\n")

for dev in devices:
    print(f"\nConnecting to {dev['ip']}...")
    conn = connect_device(dev)

    hostname_ok = check_hostname(conn)
    ntp_ok = check_ntp(conn)
    aaa_ok = check_aaa(conn)
    lo_ok = check_loopback0(conn)
    gi1_ok = check_gi1_description(conn)

    report.append(f"Device: {dev['ip']}")
    
    if hostname_ok and ntp_ok and aaa_ok and lo_ok and gi1_ok:
        print("✔ Device is fully compliant!")
        report.append("  ✔ Compliant\n")
    else:
        print("⚠ Device NOT compliant — fixing issues...")
        report.append("  ⚠ Non-Compliant – Auto-Fix Applied")

        if not hostname_ok:
            fix_hostname(conn)
            report.append("    - Hostname fixed")
        
        if not ntp_ok:
            fix_ntp(conn)
            report.append("    - NTP server added")
        
        if not aaa_ok:
            fix_aaa(conn)
            report.append("    - AAA new-model enabled")
        
        if not lo_ok:
            fix_loopback0(conn)
            report.append("    - Loopback0 configured")
        
        if not gi1_ok:
            fix_gi1_description(conn)
            report.append("    - Gi1 description updated")
        
        report.append("")

    conn.save_config()
    conn.disconnect()

# =============================
# WRITE REPORT TO FILE
# =============================

report_filename = "network_compliance_report.txt"

with open(report_filename, "w", encoding="utf-8") as file:
    for line in report:
        file.write(line + "\n")

print(f"\nCompliance report saved as {report_filename} 🚀")
