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

# 6. Commando's 
Datastores checken:

```cli
show netconf-yang datastores
````

Features checken:
```cli
show netconf-yang features
````
