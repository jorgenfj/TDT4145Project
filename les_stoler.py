hovedscenen_id = 1
gamle_scene_id = 2
hovedscenen_fil = "hovedscenen.txt"
gamle_scene_fil = "gamle-scene.txt"

def les_stolfil(filsti):
    """
    Åpner og leser innholdet av en fil som inneholder informasjon om stoler.
    Returnerer innholdet som en streng.
    """
    try:
        with open(filsti, 'r') as fil:
            filinnhold = fil.read()
            return filinnhold
    except FileNotFoundError:
        print(f"Fant ikke filen {filsti}.")

def hent_galleristoler_hovedscene():
    """
    Genererer en liste med dictionary-objekter for hver stol i galleriseksjonen på Hovedscenen.
    Hver dictionary inneholder informasjon om SalID, RadNr, SeteNr, og OmraadeNavn for stolen.
    """
    RadNr = 0
    OmraadeNavn = "Galleri"
    stoler = []
    for i in range(505, 525):
        stol = {"SalID": hovedscenen_id, "RadNr": RadNr, "SeteNr": i, "OmraadeNavn": OmraadeNavn}
        stoler.append(stol)
    return stoler

def les_parkettstoler_hovedscenen(linjer):
    """
    Tar imot en liste med linjer (tekststrenger) som representerer parkettseksjonen på Hovedscenen.
    Genererer en liste med dictionary-objekter for stoler basert på informasjonen fra linjene.
    """
    stoler = []
    for rad, linje in enumerate(linjer):
        for nr_i_linje, stolstatus in enumerate(linje.strip()):
            if stolstatus == 'x':
                continue
            stolnummer = (rad) * 28 + nr_i_linje + 1  
            stol = {"SalID": hovedscenen_id, "RadNr": rad+1, "SeteNr": stolnummer, "OmraadeNavn": "Parkett"}
            stoler.append(stol)
    return stoler

def les_stoler_gamle_scene(seksjon, galleri_seksjon_rader):
    """
    Tar imot seksjonsnavn og en liste med linjer for en gitt seksjon fra Gamle Scene.
    Genererer en liste med dictionary-objekter for hver stol i seksjonen basert på linjene.
    """
    stoler = []
    for rad, linje in enumerate(galleri_seksjon_rader):
        for seteNr, stolstatus in enumerate(linje.strip()): 
            stol = {"SalID": gamle_scene_id, "RadNr": rad+1, "SeteNr": seteNr+1, "OmraadeNavn": seksjon}
            stoler.append(stol)
    return stoler

def insett_stoler_i_database(cursor, stoler):
    """
    Tar imot en database-cursor og en liste med dictionary-objekter for stoler.
    Insetter hver stol i databasen ved hjelp av cursor-objektet.
    """
    for stol in stoler:
         cursor.execute("INSERT INTO Stol (SalID, RadNr, SeteNr, OmraadeNavn) VALUES (?, ?, ?, ?)",
                       (stol["SalID"], stol["RadNr"], stol["SeteNr"], stol["OmraadeNavn"]))

def insett_stoler_hovedscenen(cursor):
    """
    Leser filen for Hovedscenen, bearbeider informasjonen, og setter inn stoler i databasen
    for de forskjellige seksjonene.
    """
    stoler = []

    filinnhold = les_stolfil(hovedscenen_fil)
    linjer = filinnhold.split('\n')
    linjer = [linje for linje in linjer if linje.strip()]
    linjer = linjer[7:] # Skipper til Parkett seksjonen
    
    stoler.extend(hent_galleristoler_hovedscene())

    nye_stoler = les_parkettstoler_hovedscenen(linjer)

    stoler.extend(nye_stoler)

    insett_stoler_i_database(cursor, stoler)
         
def insett_stoler_gamle_scene(cursor):
    """
    Leser filen for Gamle Scene, bearbeider informasjonen for hver seksjon, og setter inn
    stoler i databasen for de forskjellige seksjonene.
    """
    stoler = []

    filinnhold = les_stolfil(gamle_scene_fil)
    linjer = filinnhold.split('\n')
    linjer = [linje for linje in linjer if linje.strip()]
    linjer = linjer[1:] # Fjerner datolinjen

    # Lager dictionary med seksjonsnavn som nøkkel og en liste med linjer fra filen som verdier
    seksjonslinjer = {}
    seksjon = ""
    for linje in linjer:
        if linje.isalpha():
            seksjon = linje
            seksjonslinjer[seksjon] = []
        else:
            seksjonslinjer[seksjon].append(linje)

    # Henter stoler for hver seksjon
    for seksjon, rader in seksjonslinjer.items():
        rader = rader[::-1] # Reverserer listen siden radnummer er synkende i filen
        nye_stoler = les_stoler_gamle_scene(seksjon, rader)
        stoler.extend(nye_stoler)

    insett_stoler_i_database(cursor, stoler)


def insett_stoler_fra_filer(cursor):
    """
    Kaller funksjonene for å sette inn stoler fra filene for både Hovedscenen og Gamle Scene.
    """
    insett_stoler_hovedscenen(cursor)
    insett_stoler_gamle_scene(cursor)