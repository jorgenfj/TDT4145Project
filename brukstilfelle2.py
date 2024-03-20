hovedscenen_id = 1
gamle_scene_id = 2
hovedscenen_file = "hovedscenen.txt"
gamle_scene_file = "gamle-scene.txt"
kjop_id_hovedscenen = 1
kjop_id_gamle_scene = 2
BillettNr = 0
hovedscenen_tid = '19:00:00'
gamle_scene_tid = '18:30:00'

def les_stolfil(filsti):
    """
    Leser innholdet av en fil som spesifisert av 'filsti' og returnerer dette innholdet som en streng.
    Hvis filen ikke finnes, skrives en feilmelding ut til konsollen.
    """
    try:
        with open(filsti, 'r') as fil:
            filinnhold = fil.read()
            return filinnhold
    except FileNotFoundError:
        print(f"Fant ikke filen {filsti}.")

def les_dato(filinnhold):
    """
    Henter ut datoen fra filinnholdet og returnerer denne som en streng.
    """
    dato = filinnhold.split('\n')[0]
    dato = dato[5:]
    return dato

def les_parkettbilletter_hovedscene(linjer):
    """
    Behandler hver linje i 'linjer' for å generere en liste med billetter for parkettstolene på Hovedscenen.
    'linjer' representerer tekststrenger hvor hver karakter indikerer om en stol er ledig ('0') eller tatt ('1').
    Returnerer en liste med dictionary-objekter, hvor hvert objekt representerer en billett.
    """
    billetter = []
    for rad, linje in enumerate(linjer):
        for nr_i_linje, stolstatus in enumerate(linje.strip()):
            if stolstatus == '1':
                stolnummer = (rad) * 28 + nr_i_linje + 1  
                billett = {"SalID": hovedscenen_id, "RadNr": rad+1, "SeteNr": stolnummer, "OmraadeNavn": "Parkett"}
                billetter.append(billett)
    return billetter

def les_seksjonsbilletter_gamle_scene(seksjon, seksjonsrader):
    """
    Genererer en liste med billetter basert på 'seksjonsrader' for en gitt 'seksjon' i Gamle Scene.
    Hver karakter i en linje indikerer om en stol er ledig ('0') eller tatt ('1').
    Returnerer en liste med dictionary-objekter, hvor hvert objekt representerer en billett.
    """
    billetter = []
    for rad, linje in enumerate(seksjonsrader):
        for seteNr, stolstatus in enumerate(linje.strip()):
            if stolstatus == '1':
                stolnummer = seteNr + 1  
                billett = {"SalID": gamle_scene_id, "RadNr": rad+1, "SeteNr": seteNr+1, "OmraadeNavn": seksjon}
                billetter.append(billett)
    return billetter


def insett_billetter_hovedscenen(cursor):
    """
    Leser filen for Hovedscenen, henter informasjon om billetter, og kaller en hjelpefunksjon for å sette inn
    disse billettene i databasen.
    Informasjon om kjøp samles i en 'kjop_info'-dictionary og sendes videre til innsettingsfunksjonen.
    """
    billetter = []
    filinnhold = les_stolfil(hovedscenen_file)
    linjer = filinnhold.split('\n')
    linjer = [linje for linje in linjer if linje.strip()]
    linjer = linjer[7:] # Skipper til Parkett seksjonen

    nye_billetter = les_parkettbilletter_hovedscene(linjer)
    billetter.extend(nye_billetter)

    kjop_info = {
        'kunde_id': 0, 
        'totalpris': 0,  
        'dato': les_dato(filinnhold),
        'tid': hovedscenen_tid,
        'teaterstykke_id': 1,  
    }

    insett_billetter_i_database(cursor, billetter, kjop_id_hovedscenen, kjop_info)

def insett_billetter_gamle_scene(cursor):
    """
    Leser filen for Gamle Scene, henter informasjon om billetter for hver seksjon, og kaller en hjelpefunksjon
    for å sette inn disse billettene i databasen.
    Informasjon om kjøp samles i en 'kjop_info'-dictionary og sendes videre til innsettingsfunksjonen.
    """
    billetter = []
    filinnhold = les_stolfil(gamle_scene_file)
    linjer = filinnhold.split('\n')
    linjer = [linje for linje in linjer if linje.strip()]
    linjer = linjer[1:]  # Skip dato linjen

    # Lager dictionary med seksjonsnavn som nøkkel og en liste med linjer fra filen som verdier
    seksjonslinjer = {}
    seksjon = ""
    for linje in linjer:
        if linje.isalpha():
            seksjon = linje
            seksjonslinjer[seksjon] = []
        else:
            seksjonslinjer[seksjon].append(linje)

    # Henter billetter for hver seksjon
    for seksjon, seksjonslinjer in seksjonslinjer.items():
        seksjonslinjer = seksjonslinjer[::-1]  # Reverserer listen siden radnummer er synkende i filen
        nye_billetter = les_seksjonsbilletter_gamle_scene(seksjon, seksjonslinjer)
        billetter.extend(nye_billetter)

    kjop_info = {
        'kunde_id': 0,  
        'totalpris': 0,
        'dato': les_dato(filinnhold),
        'tid': gamle_scene_tid,
        'teaterstykke_id': 2,
    }

    insett_billetter_i_database(cursor, billetter, kjop_id_gamle_scene, kjop_info)

def insett_billetter_i_database(cursor, billetter, KjopID, kjop_info):
    """
    Setter inn kjøpsinformasjon og billetter i databasen basert på de oppgitte parameterne.
    Funksjonen behandler innsetting av kjøpsdetaljer (Billettkjop, Teaterbillett, ReservererForestilling)
    og detaljer for hver individuelle billett (Billettype, ReservererStol).
    'KjopID' benyttes for å knytte billetter til et spesifikt kjøp.
    """
    # Innsetting av Billettkjop, Teaterbillett, og ReservererForestilling
    cursor.execute("INSERT INTO Billettkjop (KjopID, KundeID, Totalpris, Dato, Tid) VALUES (?, ?, ?, ?, ?)",
                   (KjopID, kjop_info['kunde_id'], kjop_info['totalpris'], kjop_info['dato'], kjop_info['tid']))
    cursor.execute("INSERT INTO Teaterbillett (KjopID, TeaterstykkeID) VALUES (?, ?)",
                   (KjopID, kjop_info['teaterstykke_id']))
    cursor.execute("INSERT INTO ReservererForestilling (KjopID, TeaterstykkeID, ForestillingsDato, ForestillingsTidspunkt) VALUES (?, ?, ?, ?)",
                   (KjopID, kjop_info['teaterstykke_id'], kjop_info['dato'], kjop_info['tid']))

    # Innsetting av billetter
    global BillettNr
    BillettNr = 0
    for billett in billetter:
        BillettNr += 1
        cursor.execute("INSERT INTO Billettype (KjopID, BillettNr, Type) VALUES (?, ?, 'ORDINÆR')",
                       (KjopID, BillettNr))
        cursor.execute("INSERT INTO ReservererStol (KjopID, BillettNr, SalID, RadNr, SeteNr, OmraadeNavn) VALUES (?, ?, ?, ?, ?, ?)",
                       (KjopID, BillettNr, billett["SalID"], billett["RadNr"], billett["SeteNr"], billett["OmraadeNavn"]))
        

def insett_billetter_fra_filer(cursor):
    """
    Denne funksjonen kaller funksjonene for å leses billetter fra filene for både Hovedscenen og Gamle Scene.
    Setter så disse inn i databasen.
    """
    insett_billetter_hovedscenen(cursor)
    insett_billetter_gamle_scene(cursor)

    