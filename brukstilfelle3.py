from prettytable import PrettyTable, ALL

def finn_alle_forestillinger():
    """
    Finner alle forestillinger og printer en tabell med informasjon om hver forestilling.
    """
    cursor.execute('''
        SELECT Tittel, Dato, Tidspunkt, Teatersal.Navn AS SalNavn, Forestilling.TeaterstykkeID, Teatersal.SalID
        FROM Forestilling 
        JOIN Teaterstykke ON Forestilling.TeaterstykkeID = Teaterstykke.TeaterstykkeID
        JOIN teaterSal ON Teaterstykke.SalID = TeaterSal.SalID
        ORDER BY Tittel, Dato
    ''')
    forestillinger = cursor.fetchall()
    if forestillinger == []:
        print("Ingen forestillinger funnet.")
        return
    forestillinger_tabell = PrettyTable(['Nr', 'Teaterstykke', 'Dato', 'Tidspunkt', 'Sal'])
    forestillinger_tabell.hrules = ALL

    # Legg til et unikt radnummer for hver forestilling, radnummer er 1-indeksert
    for idx, forestilling in enumerate(forestillinger, start=1):
        forestillinger_tabell.add_row([idx] + list(forestilling[:-2])) # Eksluder SalID og TeaterstykkeID fra tabellen
        
    print(f'\n {forestillinger_tabell} \n')

    return forestillinger

def velg_forestilling(forestillinger):
    """
    Velg en forestilling ved å oppgi radnummer i forestillingstabellen.
    Returnerer valgt forestilling med tittel, dato, tidspunkt, salnavn, teaterstykkeID og salID.
    """
    while True:
        valgt_forestillings_nummer = input("Velg en forestilling ved å oppgi radnummer, eller tast q for å gå tilbake: ")
        if valgt_forestillings_nummer == 'q':
            return 'q'
        try:
            valgt_forestillings_nummer = int(valgt_forestillings_nummer)
        except ValueError:
            print("Vennligst oppgi et gyldig tall.")
            continue
        # Sjekk om valgt nummer er gyldig
        if 1 <= valgt_forestillings_nummer <= len(forestillinger):
            # Hent valgt forestilling
            valgt_forestilling = forestillinger[valgt_forestillings_nummer - 1]
            teaterstykketittel, dato, tidspunkt, salnavn, teaterstykkeID, salID = valgt_forestilling
            print("\nDu har valgt forestilling:")
            print(f"Teaterstykke: {teaterstykketittel}, Dato: {dato}, Tidspunkt: {tidspunkt}, Sal: {salnavn}\n") 
            return valgt_forestilling
        else:
            print(f"\nUgyldig nummer. Velg et nummer mellom 1 og {len(forestillinger)} \n")

def print_antall_ledige_seter_i_rad(forestilling):
    """
    Henter antall ledige seter i hver rad for en gitt forestilling.
    """
    teaterstykketittel, dato, tidspunkt, salnavn, teaterstykkeID, salID = forestilling

    cursor.execute('''
        SELECT 
            Stol.RadNr, 
            Stol.OmraadeNavn, 
            (COUNT(Stol.SeteNr) - COUNT(ReservererStol.SeteNr)) as LedigeSeter
        FROM 
            Stol
        LEFT JOIN 
            ReservererStol 
            ON Stol.SalID = ReservererStol.SalID 
            AND Stol.RadNr = ReservererStol.RadNr 
            AND Stol.SeteNr = ReservererStol.SeteNr 
            AND Stol.OmraadeNavn = ReservererStol.OmraadeNavn
            AND ReservererStol.KjopID IN (
                SELECT 
                    KjopID 
                FROM 
                    ReservererForestilling 
                WHERE 
                    TeaterstykkeID = ? 
                    AND ForestillingsDato = ? 
                    AND ForestillingsTidspunkt = ?
            )
        WHERE 
            Stol.SalID = ?
        GROUP BY 
            Stol.RadNr, Stol.OmraadeNavn
        ORDER BY 
            Stol.OmraadeNavn, Stol.RadNr
    ''', (teaterstykkeID, dato, tidspunkt, salID))
    
    antall_ledige_seter_i_rad = cursor.fetchall()
    ledige_seter_tabell = PrettyTable(['RadNr', 'OmraadeNavn', 'LedigeSeter'])
    ledige_seter_tabell.hrules = ALL

     # Legg til et unikt radnummer for hver forestilling
    for rad in antall_ledige_seter_i_rad:
        ledige_seter_tabell.add_row(rad)
    print(f'\n {ledige_seter_tabell} \n')

def velg_ordre(valgt_forestilling):
    """
    Velg rad, område og antall seter for en gitt forestilling.
    """
    salID = valgt_forestilling[5]
    while True:
        print("Velg radnummer, Område og antall seter du ønsker å kjøpe, eller tast q for å gå tilbake.")
        radnummer = input("Radnummer: ")
        if radnummer.lower() == 'q':
            return 'q', 'q'
        omraade_navn = input("Område: ")
        if omraade_navn.lower() == 'q':
            return 'q', 'q'
        antall_seter_onsket = input("Antall seter: ")
        if antall_seter_onsket.lower() == 'q':
            return 'q', 'q'
    
        try:
            radnummer = int(radnummer)
            antall_seter_onsket = int(antall_seter_onsket)
        except ValueError:
            print("Vennligst oppgi gyldige tall for radnummer og antall seter.")
            continue

        # Sjekk og fjern fnutter rundt OmrådeNavn
        if (omraade_navn.startswith('"') and omraade_navn.endswith('"')) or (omraade_navn.startswith("'") and omraade_navn.endswith("'")):
            omraade_navn = omraade_navn[1:-1]

        omraade_navn = omraade_navn.capitalize()

        # Sjekke om område og rad er gyldig
        cursor.execute('''SELECT EXISTS(SELECT 1 FROM Stol WHERE SalID = ? AND OmraadeNavn = ? AND RadNr = ?)''', (salID, omraade_navn, radnummer))
        exists = cursor.fetchone()[0]

        if not exists:
            print(f"RadNr: {radnummer} finnes ikke i Område {omraade_navn}.")
            continue
        # Sjekk om kombinasjonen av brukerinput er gyldig. 
        #Gjør dette opp med databasen og ikke opp mot ledige_seter_tabell fra print_antall_ledige_seter_i_rad funksjonen.
        ledige_seter, teaterstykkeID = sjekk_ledige_seter_rad(radnummer, omraade_navn, antall_seter_onsket, valgt_forestilling)
        if ledige_seter == 'q':
            continue
        return ledige_seter, teaterstykkeID

def sjekk_ledige_seter_rad(radnummer, omraade_navn, antall_seter_onsket, valgt_forestilling):
    """
    Sjekker om det er nok ledige seter på en gitt rad for en gitt forestilling.
    """
    teaterstykketittel, dato, tidspunkt, salnavn, teaterstykkeID, salID = valgt_forestilling
    cursor.execute('''
        SELECT RadNr, OmraadeNavn, SeteNr 
        FROM Stol 
        WHERE SalID = ? AND RadNr = ? AND OmraadeNavn = ? AND SeteNr NOT IN (
            SELECT SeteNr 
            FROM ReservererStol
            WHERE SalID = ? AND RadNr = ? AND OmraadeNavn = ? AND KjopID IN (
                SELECT KjopID 
                FROM ReservererForestilling 
                WHERE TeaterstykkeID = ? AND ForestillingsDato = ? AND ForestillingsTidspunkt = ?
            )
        )
        ORDER BY SeteNr
        LIMIT ?
    ''', (salID, radnummer, omraade_navn, salID, radnummer, omraade_navn, teaterstykkeID, dato, tidspunkt, antall_seter_onsket))

    ledige_seter = cursor.fetchall()

    if len(ledige_seter) < antall_seter_onsket:
        print(f"Det er ikke nok ledige seter på den spesifiserte raden. \nAntall ledige seter er {len(ledige_seter)}, mens du ønsker å kjøpe {antall_seter_onsket} seter.")
        ledige_seter = 'q'
        return ledige_seter, teaterstykkeID
    
    return ledige_seter, teaterstykkeID

def velg_billettyper(ledige_seter, teaterstykkeID):
    """
    Velg billettyper og antall for hver billettype for en gitt forestilling.
    returnerer billett_dict og billettyper.
    billett_dict holder styr på antall billetter for hver billettype.
    billettyper er en liste med tupler av (Type, Pris) hentet fra Pristype-tabellen for det gitte teaterstykket.
    """
    cursor.execute('''
        SELECT Type, Pris
        FROM Pristype
        WHERE TeaterstykkeID = ?
    ''', (teaterstykkeID,))
    billettyper = cursor.fetchall()
    billettyper_tabell = PrettyTable(['TypeNr', 'Type', 'Pris'])
    
    # Legg til en unik radnummer for hver billettype
    for idx, billettype in enumerate(billettyper, start=1):
        billettyper_tabell.add_row([idx] + list(billettype))
    billettyper_tabell.hrules = ALL
    print(f'\n{billettyper_tabell}\n')

    billett_dict = {}
    totalt_valgte_billetter = 0

    print("Velg først billettype du ønsker ved å skrive inn 'TypeNr', deretter velg antall du ønsker for den valgte typen. Tast 'q' for å gå tilbake: ")
    while totalt_valgte_billetter < len(ledige_seter):
        try:
            # Validering for valgt billettype
            valgt_billettype = input("TypeNr: ")
            if valgt_billettype.lower() == 'q':
                return 'q', 'q'
            valgt_billettype = int(valgt_billettype)-1 # TypeNr er 1-indeksert
            if valgt_billettype < 0 or valgt_billettype >= len(billettyper):
                print("Ugyldig TypeNr, prøv igjen.")
                continue
            # Sjekk om valgt billettype er en gruppebillett og om det er nok billetter igjen i dette kjøpet for å kjøpe gruppebilletter
            if billettyper[valgt_billettype][0].startswith("Gruppe") and len(ledige_seter) - totalt_valgte_billetter < 10:
                print(f"Denne typen har et min antall på 10. Du må bestemme type for de resterende {len(ledige_seter) - totalt_valgte_billetter} billettene dine.")
                continue
            
            # Validering av antall billetter for en valgt billettype
            antall_billetter = input("Antall: ")
            if antall_billetter.lower() == 'q':
                return 'q', 'q'
            antall_billetter = int(antall_billetter)
            if antall_billetter <= 0:
                print("Ugyldig antall, prøv igjen.")
                continue
            if totalt_valgte_billetter + antall_billetter > len(ledige_seter):
                print(f"Du har valgt for mange billetter for dette kjøpet. Du må velge type for de resterende {len(ledige_seter) - totalt_valgte_billetter} billettene i kjøpet.")
                continue
            if billettyper[valgt_billettype][0].startswith("Gruppe") and antall_billetter < 10:
                print(f"Minimum antall billetter for denne billettypen er {10}. Prøv igjen.")
                continue
            
            # Henter navnet på valgt billettype. Billettyper er en liste med tupler av (Type, Pris).
            # valgt_billettype indekserer billettyper, og billettyper[valgt_billettype][0] er navnet på valgt billettype.
            billettype_navn = billettyper[valgt_billettype][0]

            # Legg til antall valgte billetter for valgt billettype i billett_dict
            # billett_dict er en dictionary med billettype_navn som nøkkel og antall_billetter som verdi.
            billett_dict[billettype_navn] = billett_dict.get(billettype_navn, 0) + antall_billetter

            # Oppdater totalt_valgte_billetter for dette kjøpet
            totalt_valgte_billetter += antall_billetter

            if totalt_valgte_billetter == len(ledige_seter):
                break
        except ValueError:
            print("Feil input, prøv igjen.")
    
    return billett_dict, billettyper

def print_billett_info_og_beregn_pris(billettype_dict, ledige_seter, billettyper, valgt_forestilling):
    """
    Printer en tabell med informasjon om billetter og beregner totalpris for kjøpet.
    Returnerer valg og billett_dict.
    """
    billett_tabell = PrettyTable(['RadNr', 'OmrådeNavn', 'SeteNr', 'Billettype', 'Pris'])
    billett_tabell.hrules = ALL
    totalpris = 0
    # Lager en kopi av billett_dict for å ikke endre originalen
    billettype_dict_kopi = billettype_dict.copy()
    # billettype_til_pris er en dictionary med billettype som nøkkel og pris som verdi.
    billettype_til_pris = {billettype[0]: billettype[1] for billettype in billettyper}

    # Itererer gjennom listen av ledige seter.
    for sete in ledige_seter:
        radnummer, omraade_navn, seteNr = sete
        # Itererer gjennom kopien av billett_dict for å finne antallet billetter igjen av hver type.
        for billettype, antall in billettype_dict_kopi.items():
            if antall > 0:
                # Henter prisen for den aktuelle billettypen.
                pris = billettype_til_pris[billettype]
                billett_tabell.add_row([radnummer, omraade_navn, seteNr, billettype, pris])
                totalpris += pris
                # Reduserer antallet billetter igjen av denne typen med 1.
                billettype_dict_kopi[billettype] -= 1
                # Bryter den indre løkken for å gå videre til neste sete
                break
    

    teaterstykketittel, dato, tidspunkt, salnavn, teaterstykkeID, salID = valgt_forestilling
    print(f'\n{billett_tabell}\n')
    print(f'Totalpris for kjøpet: {totalpris} kr')
    print(f'\nForestilling: {teaterstykketittel}, Dato: {dato}, Tidspunkt: {tidspunkt}, Sal: {salnavn}\n')
    
    valg = input("Press 1 for å logge inn eller registrere bruker. Tast 'q' for å gå tilbake: ")       
    return valg, billettype_dict

def login():
    """
    Logg inn eller registrer bruker.
    Returnerer KundeID for brukeren som er logget inn eller nylig registrert.
    """
    while True:
        print("\nVelg login eller registrer bruker: \n1 - Login\n2 - Registrer bruker\nq - Avslutt\n")
        valg = input()

        if valg == '1':
            mobilnummer = input("Mobilnummer: \n")
            cursor.execute("SELECT KundeID, Mobilnummer, Navn, Adresse FROM KundeProfil WHERE Mobilnummer = ?", (mobilnummer,))
            # Henter ut brukeren som er logget inn
            bruker = cursor.fetchone()

            if bruker:
                print("Du er logget inn.")
                return bruker[0]  # Returnerer KundeID for brukeren som er logget inn
            else:
                print("Bruker eksisterer ikke.\n")

        elif valg == '2':
            mobilnummer = input("Mobilnummer: ")
            navn = input("Navn: ")
            adresse = input("Adresse: ")

            cursor.execute("INSERT INTO KundeProfil (Mobilnummer, Navn, Adresse) VALUES (?, ?, ?)", (mobilnummer, navn, adresse))

            # Henter ut KundeID til den nylig registrerte brukeren
            kundeID = cursor.lastrowid
            print("Bruker opprettet.")
            return kundeID  # Returnerer KundeID for den nylig opprettede brukeren
        elif valg == 'q':
            return 'q'
        else:
            print("Velg et gyldig alternativ.\n")



def utfør_kjøp(valgt_forestilling, ledige_seter, billetttype_dict, billettyper, kundeID):
    """
    Utfører kjøpet og registrerer kjøpte billetter i databasen.
    """
    teaterstykketittel, dato, tidspunkt, salnavn, teaterstykkeID, salID = valgt_forestilling
    # Start transaksjon

    # Opprett et nytt kjøp i Billettkjop-tabellen
    cursor.execute('''
        INSERT INTO Billettkjop (Dato, Tid, Totalpris, KundeID)
        VALUES (CURRENT_DATE, CURRENT_TIME, ?, ?)
    ''', (0, kundeID))  # Totalpris settes midlertidig til 0 og oppdateres senere

    # Hent KjopID for det nyopprettede kjøpet
    kjopID = cursor.lastrowid

    # Registrer kjøptet i Teaterbillett-tabellen
    cursor.execute('''
        INSERT INTO TeaterBillett (KjopID, TeaterstykkeID)
        VALUES (?, ?)
    ''', (kjopID, teaterstykkeID)) 
    # Registrer kjøpet i ReservererForestilling-tabellen
    cursor.execute('''
        INSERT INTO ReservererForestilling (KjopID, TeaterstykkeID, ForestillingsDato, ForestillingsTidspunkt)
        VALUES (?, ?, ?, ?)
    ''', (kjopID, teaterstykkeID, dato, tidspunkt))

    totalpris = 0
    billettNr = 1
    # billetttype_til_pris er en dictionary med billettype som nøkkel og pris som verdi.
    billettype_til_pris = {billettype[0]: billettype[1] for billettype in billettyper}

    # Registrer hvilke seter som er reservert og tilhørende billettype
    for sete in ledige_seter:
        radnummer, omraade_navn, seteNr = sete
        # Finn en billetttype som er igjen i billett_dict og reserver sete for denne billettypen
        # Legger til prisen for billetten i totalpris og reduserer antall billetter igjen for denne billettypen
        for billettype, antall in billetttype_dict.items():
            if antall > 0:
                pris = billettype_til_pris[billettype]
                totalpris += pris
                billetttype_dict[billettype] -= 1

                # Registrer sete og billettype
                cursor.execute('''
                    INSERT INTO ReservererStol (KjopID, BillettNr, SalID, RadNr, SeteNr, OmraadeNavn)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (kjopID, billettNr, salID, radnummer, seteNr, omraade_navn))
                print(kjopID, billettNr, salID, radnummer, seteNr, omraade_navn)
                cursor.execute('''
                    INSERT INTO Billettype (KjopID, BillettNr, Type)
                    VALUES (?, ?, ?)
                ''', (kjopID, billettNr, billettype))
                
                billettNr += 1
                break  # Gå til neste sete etter at billetttype er tildelt

    # Oppdater totalpris i Billettkjop
    cursor.execute('''
        UPDATE Billettkjop
        SET Totalpris = ?
        WHERE KjopID = ?
    ''', (totalpris, kjopID))
        
    print("Kjøpet ble utført.")


def billettkjop_system(ekstern_cursor):
    """
    Billettkjøp-systemet som lar en bruker kjøpe et antall billetter innenfor en rad for en gitt forestilling.
    """
    global cursor 
    cursor = ekstern_cursor
    print("Velkommen til billettkjøp!")
    while True:
        forestillinger = finn_alle_forestillinger()
        if forestillinger == None:
            print("ERROR: Ingen forestillinger funnet.")
            return

        valgt_forestilling = velg_forestilling(forestillinger)
        if valgt_forestilling == 'q':
            break

        while True:
            print_antall_ledige_seter_i_rad(valgt_forestilling)
            
            ledige_seter, teaterstykkeID = velg_ordre(valgt_forestilling)
            if ledige_seter == 'q':
                break
            
            while True:
                billettype_dict, billettyper = velg_billettyper(ledige_seter, teaterstykkeID)
                if billettype_dict == 'q':
                    break
                
                while True:
                    valg, billettype_dict = print_billett_info_og_beregn_pris(billettype_dict, ledige_seter, billettyper, valgt_forestilling)
                    if valg.lower() == 'q':
                        break
                    
                    while True:
                        kundeID = login()
                        if kundeID == 'q':
                            break

                        utfør_kjøp(valgt_forestilling, ledige_seter, billettype_dict, billettyper, kundeID)
                        return
