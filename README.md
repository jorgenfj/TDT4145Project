# Prosjektet er laget av

- Søren Boucher
- Jørgen Fjermedal
- Herman Østenby

# Prosjektoppsettguide

Denne veiledningen vil hjelpe deg med å sette opp databasen og installere de nødvendige Python-pakkene for dette prosjektet.

## Oppsett av database

Følg disse stegene for å sette opp SQLite-databasen for dette prosjektet:

1. **Last ned SQLite3**
   - **VSCode**
      - Last ned SQLite-extension i VSCode

2. **Opprett databasen**
   - Åpne en terminal eller kommandoprompt.
   - Naviger til mappen der du har lastet ned prosjektet.
   - For å opprette databasen fra SQL-scriptet, kjør main()-funksjonen i main.py. I terminalen blir du spurt om å velge en funksjon. Tast 0.

## Installasjon av Python og pip

Sørg for at du har Python installert på systemet ditt. Pip (Pythons pakkeinstallatør) er inkludert med Python. For å sjekke om du har Python og pip installert, kan du kjøre følgende kommandoer i terminalen eller kommandoprompten:

```shell
python --version
pip --version
```

Hvis du ikke har Python installert, last ned og installer det fra [den offisielle Python-nettsiden](https://www.python.org/downloads/). Under installasjonsprosessen, sørg for å velge alternativet for å legge Python til systemets PATH.

## Installasjon av PrettyTable

PrettyTable er et Python-bibliotek som lar deg enkelt vise tabulære data. Følg disse stegene for å installere PrettyTable:

1. **Åpne en terminal eller kommandoprompt**
   - Sørg for at du har installert Python og pip ved å følge stegene ovenfor.

2. **Installer PrettyTable**
   - Kjør følgende kommando:
     ```shell
     pip install prettytable
     ```

Prosjektet er nå korrekt satt opp med SQLite og PrettyTable.

## Hvordan bruke programmet
All funksjonalitet kjøres gjennom main()-funksjonen i main.py. Kjør derfor denne filen for å starte programmet.

Ved oppstart får man 8 valg av programmer som kan kjøres.

 - 0 - Nullstill og lag tomme tabeller

 - 1 - Brukstilfelle 1: Fyll inn tabellene med data

 - 2 - Brukstilfelle 2: Legg inn seter fra gitt .txt filer

 - 3 - Brukstilfelle 3: Kjøp billetter til en forestilling

 - 4 - Brukstilfelle 4: Søk på forestilling etter dato

 - 5 - Brukstilfelle 5: Navn på skuespillere i forskjellige teaterstykker

 - 6 - Brukstilfelle 6: Best solgt forestilling

 - 7 - Brukstilfelle 7: Skuespiller som har spilt med i samme akt

 **NB! Brukerhistorie 0 og 1 må kjøres før noen av de andre vil fungere.**

 ## Tekstlige resultater fra brukerhistorier
 Alle tekstlige resultater fra spørringer ligger vedlagt i brukstilfellerOutput.pdf