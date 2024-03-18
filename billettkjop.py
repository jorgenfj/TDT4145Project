import sqlite3
from prettytable import PrettyTable, ALL
from program import login
# Opprett en databaseforbindelse
con = sqlite3.connect("teater.db")
cursor = con.cursor()


def finn_alle_forestillinger():
    """
    Finn alle forestillinger.
    """
    cursor.execute('''
        SELECT Tittel, Dato, Tidspunkt, Teatersal.Navn AS SalNavn, Forestilling.TeaterstykkeID, Teatersal.SalID
        FROM Forestilling 
        JOIN Teaterstykke ON Forestilling.TeaterstykkeID = Teaterstykke.TeaterstykkeID
        JOIN teaterSal ON Teaterstykke.SalID = TeaterSal.SalID
    ''')
    forestillinger = cursor.fetchall()
    if forestillinger == []:
        print("Ingen forestillinger funnet.")
        return
    forestillinger_tabell = PrettyTable(['Nr', 'Teaterstykke', 'Dato', 'Tidspunkt', 'Sal'])
    forestillinger_tabell.hrules = ALL

    # Legg til en unik radnummer for hver forestilling
    for idx, forestilling in enumerate(forestillinger, start=1):
        forestillinger_tabell.add_row([idx] + list(forestilling[:-2])) # Eksluder SalID og TeaterstykkeID fra tabellen
        
    print(f'\n {forestillinger_tabell} \n')
    return forestillinger

def velg_forestilling(forestillinger):
    """
    Velg en forestilling basert på oppgitt radnummer.
    """
    while True:
        # Be brukeren om å velge en forestilling ved å oppgi radnummer
        valgt_forestillings_nummer = input("Velg en forestilling ved å oppgi nummer, eller press q for å gå tilbake: ")
        if valgt_forestillings_nummer == 'q':
            return 'q'
        try:
            valgt_forestillings_nummer = int(valgt_forestillings_nummer)
        except ValueError:
            print("Vennligst oppgi et gyldig tall.")

        if 1 <= valgt_forestillings_nummer <= len(forestillinger):
            valgt_forestilling = forestillinger[valgt_forestillings_nummer - 1]
            print("\nDu har valgt forestilling:")
            print(f"Teaterstykke: {valgt_forestilling[0]}, Dato: {valgt_forestilling[1]}, Tidspunkt: {valgt_forestilling[2]}, Sal: {valgt_forestilling[3]}\n") 
            return valgt_forestilling
        else:
            print(f"\nUgyldig nummer. Velg et nummer mellom 1 og {len(forestillinger)} \n")

def print_antall_ledige_seter_i_rad(forestilling):
    """
    Hent antall ledige seter i hver rad for en gitt forestilling.
    forestilling[1] er dato, forestilling[2] er tid, forestilling[3] er salID og forestilling[4] er teaterstykkeID
    """
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
    ''', (forestilling[4], forestilling[1], forestilling[2], forestilling[5]))
    
    antall_ledige_seter_i_rad = cursor.fetchall()
    ledige_seter_tabell = PrettyTable(['RadNr', 'OmraadeNavn', 'LedigeSeter'])
    ledige_seter_tabell.hrules = ALL

     # Legg til en unik radnummer for hver forestilling
    for rad in antall_ledige_seter_i_rad:
        ledige_seter_tabell.add_row(rad)
    print(f'\n {ledige_seter_tabell} \n')

def velg_ordre(valgt_forestilling):
    """
    Velg rad og antall seter for en gitt forestilling.
    """
    while True:
        print("Velg radnummer, Område og antall seter du ønsker å kjøpe, eller skriv q for å gå tilbake.")
        # ordre = input("Skriv inn radnummer, OmraadeNavn og antall seter du ønsker å kjøpe, på format (RadNr,OmraadeNavn,AntallSeter): ")
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

        # Sjekke og fjerne fnutter rundt OmrådeNavn
        if (omraade_navn.startswith('"') and omraade_navn.endswith('"')) or (omraade_navn.startswith("'") and omraade_navn.endswith("'")):
            omraade_navn = omraade_navn[1:-1]

        omraade_navn = omraade_navn.capitalize()

        # Sjekke om område og rad er gyldig
        cursor.execute('''SELECT EXISTS(SELECT 1 FROM Stol WHERE SalID = ? AND OmraadeNavn = ? AND RadNr = ?)''', (valgt_forestilling[5], omraade_navn, radnummer))
        exists = cursor.fetchone()[0]

        if not exists:
            print(f"RadNr: {radnummer} finnes ikke i Område {omraade_navn}.")
            continue


        ledige_seter, teaterstykkeID = sjekk_ledige_seter_rad(radnummer, omraade_navn, antall_seter_onsket, valgt_forestilling)
        if ledige_seter == 'q':
            continue
        return ledige_seter, teaterstykkeID

def sjekk_ledige_seter_rad(radnummer, omraade_navn, antall_seter_onsket, valgt_forestilling):
    # Finn ledige seter på ønsket rad og område
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
    ''', (valgt_forestilling[5], radnummer, omraade_navn, valgt_forestilling[5], radnummer, omraade_navn, valgt_forestilling[4], valgt_forestilling[1], valgt_forestilling[2], antall_seter_onsket))

    ledige_seter = cursor.fetchall()

    if len(ledige_seter) < antall_seter_onsket:
        print(f"Det er ikke nok ledige seter på den spesifiserte raden. \nAntall ledige seter er {len(ledige_seter)}, mens du ønsker å kjøpe {antall_seter_onsket} seter.")
        ledige_seter = 'q'
        return ledige_seter, valgt_forestilling[4]
    
    return ledige_seter, valgt_forestilling[4]

def velg_billettyper(ledige_seter, teaterstykkeID):
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

    print("Velg først billettype du ønsker ved å skrive inn 'TypeNr', deretter antall. Skriv 'q' for å avbryte: ")
    while totalt_valgte_billetter < len(ledige_seter):
        try:
            valgt_billettype = input("TypeNr: ")
            if valgt_billettype.lower() == 'q':
                return 'q', 'q'
            valgt_billettype = int(valgt_billettype)-1 # TypeNr er 1-indeksert
            if valgt_billettype < 0 or valgt_billettype >= len(billettyper):
                print("Ugyldig TypeNr, prøv igjen.")
                continue
            if billettyper[valgt_billettype][0].startswith("Gruppe") and len(ledige_seter) - totalt_valgte_billetter < 10:
                print(f"Denne typen har et min antall på 10. Du må bestemme type for de resterende {len(ledige_seter) - totalt_valgte_billetter} billettene.")
                continue
            
            antall_billetter = input("Antall: ")
            if antall_billetter.lower() == 'q':
                return 'q', 'q'
            antall_billetter = int(antall_billetter)
            if antall_billetter <= 0:
                print("Ugyldig antall, prøv igjen.")
                continue
            if totalt_valgte_billetter + antall_billetter > len(ledige_seter):
                print(f"Du har valgt for mange billetter for dette kjøpet. Du må velge {len(ledige_seter) - totalt_valgte_billetter} billetter til.")
                continue
            if billettyper[valgt_billettype][0].startswith("Gruppe") and antall_billetter < 10:
                print(f"Minimum antall billetter for denne billettypen er {10}. Prøv igjen.")
                continue

            billettype_navn = billettyper[valgt_billettype][0]
            billett_dict[billettype_navn] = billett_dict.get(billettype_navn, 0) + antall_billetter
            totalt_valgte_billetter += antall_billetter

            if totalt_valgte_billetter == len(ledige_seter):
                break
        except ValueError:
            print("Feil input, prøv igjen.")
    
    return billett_dict, billettyper

def print_billett_info_og_beregn_pris(billettype_dict, ledige_seter, billettyper, valgt_forestilling):
    billett_tabell = PrettyTable(['RadNr', 'OmrådeNavn', 'SeteNr', 'Billettype', 'Pris'])
    billett_tabell.hrules = ALL
    totalpris = 0
    billettype_dict_kopi = billettype_dict.copy()
    billettype_til_pris = {billettype[0]: billettype[1] for billettype in billettyper}

    for sete in ledige_seter:
        radnummer, omraade_navn, seteNr = sete
        for billettype, antall in billettype_dict_kopi.items():
            if antall > 0:
                pris = billettype_til_pris[billettype]
                billett_tabell.add_row([radnummer, omraade_navn, seteNr, billettype, pris])
                totalpris += pris
                billettype_dict_kopi[billettype] -= 1
                break
    
    print(f'\n{billett_tabell}\n')
    print(f'Totalpris for kjøpet: {totalpris} kr')
    print(f'\nForestilling: {valgt_forestilling[0]}, Dato: {valgt_forestilling[1]}, Tidspunkt: {valgt_forestilling[2]}, Sal: {valgt_forestilling[3]}\n')
    valg = input("Press 1 for å gå videre. Press q for å gå tilbake til hovedsiden: ")       
    return valg, billettype_dict



def utfør_kjøp(valgt_forestilling, ledige_seter, billetttype_dict, billettyper):

    # Start transaksjon
    con.execute('BEGIN;')
    
    try:
        kundeID = login(cursor)
        if kundeID == 'q':
            con.rollback()
            return
        # 1. Opprett et nytt kjøp i Billettkjop-tabellen
        cursor.execute('''
            INSERT INTO Billettkjop (Dato, Tid, Totalpris, KundeID)
            VALUES (CURRENT_DATE, CURRENT_TIME, ?, ?)
        ''', (0, kundeID))  # Totalpris settes midlertidig til 0 og oppdateres senere

        # Hent KjopID for det nyopprettede kjøpet
        kjopID = cursor.lastrowid

        # Registrer kjøpte billetter i Teaterbillett-tabellen
        cursor.execute('''
            INSERT INTO TeaterBillett (KjopID, TeaterstykkeID)
            VALUES (?, ?)
        ''', (kjopID, valgt_forestilling[4]))  # valgt_forestilling[4] inneholder TeaterstykkeID

        cursor.execute('''
            INSERT INTO ReservererForestilling (KjopID, TeaterstykkeID, ForestillingsDato, ForestillingsTidspunkt)
            VALUES (?, ?, ?, ?)
        ''', (kjopID, valgt_forestilling[4], valgt_forestilling[1], valgt_forestilling[2]))

        totalpris = 0
        billettNr = 1
        billettype_til_pris = {billettype[0]: billettype[1] for billettype in billettyper}

        # Registrer hvilke seter som er reservert og tilhørende billettype
        for sete in ledige_seter:
            radnummer, omraade_navn, seteNr = sete
            # Finn en ledig billetttype for dette setet
            for billettype, antall in billetttype_dict.items():
                if antall > 0:
                    print(billettype)
                    print(billettyper)
                    pris = billettype_til_pris[billettype]
                    totalpris += pris
                    billetttype_dict[billettype] -= 1

                    # Registrer sete og billettype
                    cursor.execute('''
                        INSERT INTO ReservererStol (KjopID, BillettNr, SalID, RadNr, SeteNr, OmraadeNavn)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (kjopID, billettNr, valgt_forestilling[5], radnummer, seteNr, omraade_navn))
                    print(kjopID, billettNr, valgt_forestilling[5], radnummer, seteNr, omraade_navn)
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
        
        # Commit transaksjonen
        con.commit()
        print("Kjøpet ble vellykket utført.")
        
    except sqlite3.Error as e:
        # Hvis noe går galt, rollback
        print("En feil oppstod under kjøpsprosessen:", e)
        con.rollback()

   



def main():
    print("Velkommen til billettkjøp!")
    while True:
        forestillinger = finn_alle_forestillinger()
        if forestillinger == None:
            print("ERROR: Ingen forestillinger funnet.")
            return

        valgt_forestilling = velg_forestilling(forestillinger)
        if valgt_forestilling == 'q':
            break

        print_antall_ledige_seter_i_rad(valgt_forestilling)
        
        ledige_seter, teaterstykkeID = velg_ordre(valgt_forestilling)
        if ledige_seter == 'q':
            continue

        billettype_dict, billettyper = velg_billettyper(ledige_seter, teaterstykkeID)
        if billettype_dict == 'q':
            continue

        valg, billettype_dict = print_billett_info_og_beregn_pris(billettype_dict, ledige_seter, billettyper, valgt_forestilling)
        if valg.lower() == 'q':
            return

        utfør_kjøp(valgt_forestilling, ledige_seter, billettype_dict, billettyper)
        return
            

main()
