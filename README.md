# Networks_Expert_LAB3

---

## Part 1: Install the virtual lab environment 

### Task Preparation and Implementation`
Oracle VirtualBox werd succesvol gedownload en geïnstalleerd met de standaardinstellingen. Daarna werd de DEVASC virtual machine correct geïmporteerd in VirtualBox via de optie Import Appliance. Het importproces verliep zonder onderbrekingen en de VM werd correct toegevoegd aan de VirtualBox-omgeving.

### Task Troubleshooting
Tijdens de installatie en het importeren van de DEVASC VM zijn geen problemen of foutmeldingen opgetreden. Alle stappen konden volgens de instructies worden uitgevoerd en troubleshooting was niet nodig.

### Task Verification
Na de installatie werd de DEVASC VM succesvol gestart. Het Ubuntu-besturingssysteem laadde correct en de grafische interface was toegankelijk. Dit bevestigt dat de virtuele labomgeving correct is geïnstalleerd en klaar is voor gebruik in de volgende onderdelen van het lab.

---

## Part 2: Install the CSR1000v VM 

### Task Preparation and Implementation
De CSR1000v virtual machine werd succesvol geïnstalleerd in VirtualBox volgens de opgegeven instructies. De juiste ISO werd gekoppeld aan de eerste CD-drive en de standaard VM-instellingen werden behouden. Na het opstarten laadde Cisco IOS-XE correct en de router was bereikbaar via het console-scherm. De initiële configuratie verliep erg straightforward en zonder extra aanpassingen.

### Task Troubleshooting
Tijdens de installatie en configuratie van de CSR1000v VM zijn geen problemen of foutmeldingen opgetreden. Alle stappen konden zonder onderbrekingen worden uitgevoerd en troubleshooting was niet noodzakelijk.

### Task Verification
De installatie werd succesvol geverifieerd door meerdere testen:
    - De CSR1000v kreeg automatisch een geldig IPv4-adres via DHCP.
    - De DEVASC VM kon de CSR1000v succesvol pingen zonder packet loss.
    - Een SSH-sessie vanuit de DEVASC VM naar de CSR1000v werd succesvol opgezet en werkte correct.
    - De WebUI van de CSR1000v was bereikbaar via HTTPS, zowel vanuit de DEVASC VM als vanaf de lokale computer.
Deze resultaten bevestigen dat de CSR1000v VM correct is geïnstalleerd en volledig operationeel is.
---

## Part 3: Python Network automation with NETMIKO 

### Task Preparation and Implementation
De vereiste omgeving was reeds correct opgezet binnen de DEVASC virtual machine. Python en de benodigde NETMIKO-bibliotheek waren beschikbaar en klaar voor gebruik. De NETMIKO-scripts konden zonder aanvullende configuratie worden uitgevoerd en maakten succesvol verbinding met de netwerkapparaten. De automatiseringstaken werden volgens de instructies uitgevoerd en verliepen op een duidelijke en rechtlijnige manier.

### Task Troubleshooting
De uitvoering van deze taak was erg straightforward. Er zijn geen fouten, connectieproblemen of configuratie-issues opgetreden tijdens het gebruik van NETMIKO. Troubleshooting was daardoor niet nodig.

### Task Verification
De resultaten van de NETMIKO-automatisering bevestigen dat de taken succesvol zijn uitgevoerd. De scripts leverden de verwachte output op en de netwerkapparaten reageerden correct op de geautomatiseerde commando’s. Dit bevestigt dat Python Network Automation met NETMIKO correct functioneert binnen de labomgeving.

---

## Part 4: Explore YANG Models 

### Task Preparation and Implementation

### Task Troubleshooting

### Task Verification

---

## Part 5: Use NETCONF to Access an IOS XE Device 

### Task Preparation and Implementation

### Task Troubleshooting

### Task Verification

---

## Part 6: Use RESTCONF to Access an IOS XE Device 

### Task Preparation and Implementation

### Task Troubleshooting

### Task Verification

---

## Part 7: Getting started with NETCONF/YANG – Part 1 

### Task Preparation and Implementation

### Task Troubleshooting

### Task Verification

---

## Part 8: Getting started with NETCONF/YANG – Part 2 

### Task Preparation and Implementation

### Task Troubleshooting

### Task Verification


---
