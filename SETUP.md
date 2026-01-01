# LOCAL EASY SETUP NO INTERNET

## ROUTER

hostname LAB-RA06-A02-R01

! ---------- Enable SSH ----------
ip domain name data.labnet.local
username student privilege 15 secret lab123
crypto key generate rsa modulus 2048
ip ssh version 2

line vty 0 4
 login local
 transport input ssh
exit

! ---------- Router-on-a-stick ----------
interface GigabitEthernet0/0/0
 no shutdown

interface GigabitEthernet0/0/0.10
 encapsulation dot1Q 10
 ip address 172.16.6.129 255.255.255.240

interface GigabitEthernet0/0/0.20
 encapsulation dot1Q 20
 ip address 172.16.6.145 255.255.255.240

interface GigabitEthernet0/0/0.30
 encapsulation dot1Q 30
 ip address 172.16.6.161 255.255.255.240

interface GigabitEthernet0/0/0.40
 encapsulation dot1Q 40
 ip address 172.16.6.177 255.255.255.240

---

## SWITCH

hostname LAB-RA06-A02-SW01
ip domain name data.labnet.local

! --- SSH ---
username student privilege 15 secret lab123
crypto key generate rsa modulus 2048
ip ssh version 2

line vty 0 4
 login local
 transport input ssh
exit

! --- VLANs ---
vlan 10
 name Management
vlan 20
 name VM-Hosts
vlan 30
 name Appliance-Servers
vlan 40
 name Data-Users

! --- Management SVI ---
interface vlan 10
 ip address 172.16.6.132 255.255.255.240
 no shutdown

ip default-gateway 172.16.6.129

! --- Access ports (Laptop on VLAN 10) ---
interface GigabitEthernet1/0/1
 description ### LAPTOP ###
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 no shutdown

! --- Trunk to router ---
interface GigabitEthernet1/0/20
 description ### UPLINK TO ROUTER ###
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40
 no shutdown

---

## PATCHING

Router:  GigabitEthernet0/0/0
   ↕
Switch:  GigabitEthernet1/0/20

Laptop Ethernet NIC
   ↕
Switch: GigabitEthernet1/0/1

## CONFIGURE IP MANUALLY

IP address:      172.16.6.131
Subnet mask:     255.255.255.240
Default gateway: 172.16.6.129
DNS:             (leave empty or 8.8.8.8)

--> disable everything: ipconfig om te kijken of het klopt

Ethernet adapter Ethernet:
   Connection-specific DNS Suffix  . : home
   Link-local IPv6 Address . . . . . : fe80::29a7:d8f6:b9ba:94b3%8
   IPv4 Address. . . . . . . . . . . : 172.16.6.131
   Subnet Mask . . . . . . . . . . . : 255.255.255.240
   Default Gateway . . . . . . . . . : 172.16.6.129

## DEBUG

SWITCH:
    show interfaces trunk
    show vlan brief
    show ip interface brief

    show interfaces gigabitEthernet1/0/20 status
    show interfaces gigabitEthernet1/0/1 status

ROUTER:
    show ip interface brief



