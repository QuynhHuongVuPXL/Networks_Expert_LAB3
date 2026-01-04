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
De DEVASC virtual machine werd succesvol opgestart en de benodigde tools, waaronder pyang, waren beschikbaar. Het YANG-model ietf-interfaces.yang werd gedownload vanaf GitHub en lokaal opgeslagen. Met behulp van pyang werd het YANG-bestand omgezet naar een boomstructuur (tree format), waardoor de opbouw van het model eenvoudig te analyseren was. Door het volgen van de beschreven stappen konden de belangrijkste containers, lists en leaf-nodes overzichtelijk worden bekeken.

### Task Troubleshooting
Tijdens deze opdracht zijn geen problemen of foutmeldingen opgetreden. Het verkennen van het YANG-model was voornamelijk een kwestie van de stappen correct volgen. Eventuele meldingen over ontbrekende modules hadden geen invloed op het bekijken van de tree-structuur en konden veilig genegeerd worden.

### Task Verification
De opdracht werd succesvol geverifieerd doordat het YANG-model correct werd weergegeven in tree-format. Belangrijke elementen zoals interfaces, interface-namen en status-attributen waren duidelijk zichtbaar. Dit bevestigt dat het YANG-model correct is geladen en dat pyang correct functioneert binnen de labomgeving.

---

## Part 5: Use NETCONF to Access an IOS XE Device 

### Task Preparation and Implementation
De NETCONF-omgeving was correct opgezet en de verbinding met het IOS XE-apparaat werd succesvol tot stand gebracht met behulp van ncclient. Met NETCONF werden configuratiegegevens opgehaald en aangepast via YANG-gebaseerde XML-structuren. De taken konden volgens de instructies worden uitgevoerd en de configuratiewijzigingen werden correct toegepast op het device.

### Task Troubleshooting
Er zijn geen functionele problemen opgetreden tijdens deze opdracht. De enige uitdaging was het werken met de YANG/XML-structuur, die vrij uitgebreid en gedetailleerd is en daardoor soms wat onoverzichtelijk en irritant kan aanvoelen. Dit had echter geen invloed op de werking van NETCONF of het eindresultaat.

### Task Verification
De correcte werking van NETCONF werd bevestigd door:
    - Het succesvol ophalen van de running configuration
    - Het aanpassen van configuratie-elementen via edit-config
    - Het correct afwijzen van een ongeldige configuratie (duplicate IP-adres)
Deze resultaten bevestigen dat NETCONF correct functioneert en dat configuraties betrouwbaar en consistent worden toegepast op het IOS XE-apparaat.

---

## Part 6: Use RESTCONF to Access an IOS XE Device 

### Task Preparation and Implementation
Voor deze taak werd de RESTCONF-service op het IOS XE-toestel gecontroleerd en correct geconfigureerd. Vervolgens werd Postman gebruikt om RESTCONF-requests te versturen naar het toestel. Met behulp van GET-requests werd interface-informatie succesvol opgehaald in JSON-formaat. Daarna werd een PUT-request gebruikt om een nieuwe loopbackinterface aan te maken. De juiste headers, authenticatie en JSON-body werden ingesteld volgens het lab.

### Task Troubleshooting
Er zijn geen functionele problemen opgetreden met het toestel of de RESTCONF-service. Wel was het enigszins frustrerend om in Postman exact de juiste combinatie van URL, headers en body te gebruiken voor de GET- en PUT-requests. Kleine fouten in het pad of de JSON-structuur leidden snel tot foutmeldingen. Na het zorgvuldig volgen van de stappen en het corrigeren van deze details werkten de requests echter zoals verwacht.

### Task Verification
De werking werd succesvol geverifieerd doordat de GET-requests correcte JSON-responses teruggaven en de PUT-request resulteerde in een HTTP 201 Created status. Daarnaast werd via de CLI op het IOS XE-toestel bevestigd dat de nieuwe loopbackinterface correct was aangemaakt en actief was.

---


