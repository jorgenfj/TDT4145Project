


def login(cursor):
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
            # con.commit() commit her eller etter kjøp? ------------------------------------------------------------------------------------------------------------------------------------------------------------------

            # Henter ut KundeID til den nylig registrerte brukeren
            kundeID = cursor.lastrowid
            print("Bruker opprettet.")
            return kundeID  # Returnerer KundeID for den nylig opprettede brukeren
        elif valg == 'q':
            return 'q'
        else:
            print("Velg et gyldig alternativ.\n")



