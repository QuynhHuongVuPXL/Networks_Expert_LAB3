# NETCONF – Candidate Datastore Enable & Verification (IOS-XE)

## Doel
Voor deze opdracht is het **NETCONF candidate datastore** vereist zodat configuraties:
- atomair gedeployed worden
- eerst gestaged worden (candidate)
- pas actief worden na een expliciete commit

Standaard is de candidate datastore **niet altijd ingeschakeld** op IOS-XE en moet deze expliciet geactiveerd worden.

---

## 1. Candidate datastore inschakelen

Ga op het IOS-XE toestel in configuratiemodus en activeer de feature:

```cli
conf t
 netconf-yang
 netconf-yang feature candidate-datastore
end
write memory
````

Uitleg:
    - netconf-yang → activeert NETCONF/YANG subsystem
    - netconf-yang feature candidate-datastore → schakelt candidate datastore in
    - write memory → zorgt dat de feature behouden blijft na reboot

## 2. NETCONF subsystem herstarten (belangrijk)
Na het enablen van de candidate feature moet NETCONF herstart worden zodat
de capabilities opnieuw geadverteerd worden aan clients.

```cli
conf t
 no netconf-yang
 netconf-yang
end
````

Zonder deze stap blijft de candidate capability vaak onzichtbaar voor NETCONF-clients.

## 3. Verificatie: datastores controleren
Controleer welke datastores beschikbaar zijn:

```cli
show netconf-yang datastores
````

Verwachte output (voorbeeld):

```cli
Datastores:
  running
  candidate
````

De aanwezigheid van candidate bevestigt dat de feature correct is geactiveerd.

## 4. Verificatie: NETCONF features controleren (optioneel)

```cli
show netconf-yang features
````

Je zou een entry moeten zien voor:

```cli
candidate-datastore
````

## 5. Verificatie vanuit NETCONF client (Python)
Wanneer een NETCONF client (bv. ncclient) verbindt, moet deze capability zichtbaar zijn:

```cli
urn:ietf:params:netconf:capability:candidate:1.0
Zonder deze capability zal een script dat de candidate datastore vereist correct stoppen met een foutmelding.
````

# 6. Verificatie

## 1. Hostname verifiëren

```cli
show running-config | section hostname
````

![show running-config](/lab4/images/show_running_config.png)

## 2. Interfaces en IP-adressen verifiëren

```cli
show ip interface brief | include Loopback
````

![show ip interface brief](/lab4/images/show_ip_interface_brief.png)

## 3. OSPF proces verifiëren

```cli
show ip ospf
````

![show ip ospf](/lab4/images/show_ip_ospf.png)

## 4. NETCONF sessie verifiëren

```cli
show netconf-yang sessions
````

![show netconf-yang sessions](/lab4/images/show_netconf_yang_sessions.png)


## 5. Candidate datastore bevestigen

```cli
show netconf-yang datastores
````

![show netconf-yang datastores](/lab4/images/show_netconf_yang_datastores.png)

# 7. Bewijs

Wanneer er geen candidate is:
![CLI fail](/lab4/images/deploy_if_fail.png)

Wanneer er wel een candidate is: 
![CLI success](/lab4/images/deploy_if_success.png)
