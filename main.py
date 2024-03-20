import sqlite3
from lag_tabeller_teater import lag_tabeller_teater
from brukstilfelle1_fyll_database import fyll_database
from brukstilfelle1_les_stoler import insett_stoler_fra_filer
from brukstilfelle2 import insett_billetter_fra_filer
from brukstilfelle3 import billettkjop_system
from brukstilfelle4 import spor_om_dato
from brukstilfelle5 import skuespillere_i_teaterstykker
from brukstilfelle6 import mest_solgt_forestilling
from brukstilfelle7 import skuespillere_i_samme_akt

db_fil = 'teater.db'
sql_script_fil = 'lag_tabeller_teater.sql'

con = sqlite3.connect(db_fil)
cursor = con.cursor()
con.execute('PRAGMA foreign_keys = ON')

def main():
    program = None
    print('\nVelkommen til Trøndelag Teater!')
    while True:
        if program == 'q':
            break
        print('\nDu har 8 valg, trykk tallet som korresponderer til ønsket handling:')
        print('Du kan taste q for å gå tilbake i interaktive programmer, eller ^C for å avbryte programmet.')
        print('''
0 - Nullstill og lag tomme tabeller 
1 - Brukstilfelle 1: Fyll inn tabellene med data
2 - Brukstilfelle 2: Legg inn seter fra gitt .txt filer
3 - Brukstilfelle 3: Kjøp billetter til en forestilling
4 - Brukstilfelle 4: Søk på forestilling etter dato
5 - Brukstilfelle 5: Navn på skuespillere i forskjellige teaterstykker
6 - Brukstilfelle 6: Best solgt forestilling
7 - Brukstilfelle 7: Skuespiller som har spilt med i samme akt
            ''')
        while True:
            program = input('Tast inn et tall: ')
            if program == 'q':
                break
            try:
                program = int(program)
                if program < 0 or program > 7:
                    print('Skriv inn et gyldig tall fra 0-7')
                    continue
            except ValueError:
                print('Skriv inn et gyldig tall fra 0-7')
                continue
            if program == 0:
                try:
                    lag_tabeller_teater(sql_script_fil, cursor)
                    con.commit()
                    print('Tabellene er laget i filen teater.db')
                except Exception as e:
                    print(f"ERROR: {e}")
                    con.rollback()
                continue
            elif program == 1:
                try:
                    fyll_database(cursor) 
                    insett_stoler_fra_filer(cursor)
                    con.commit()
                    print('Databasen er fylt med data')
                except Exception as e:
                    if "UNIQUE constraint failed" in str(e):
                        print("ERROR: UNIQUE Constrant har oppstått.\n Vennligst tøm databasen først for å kjøre denne en gang til.")
                    else:
                        print(f"ERROR: {e}")
                    con.rollback()
                continue
            elif program == 2:
                try:
                    insett_billetter_fra_filer(cursor)
                    con.commit()
                    print('Billettene er lagt til i databasen')
                except Exception as e:
                    if "UNIQUE constraint failed" in str(e):
                        print("ERROR: UNIQUE Constrant har oppstått.\n Vennligst tøm databasen først for å kjøre denne en gang til.")
                    else:
                        print(f"ERROR: {e}")
                    con.rollback()
                continue
            elif program == 3: 
                try:
                    billettkjop_system(cursor)
                    con.commit()
                except Exception as e:
                    print(f"ERROR: {e}")
                    con.rollback()
                input("Trykk enter for å gå tilbake")
                break
            elif program == 4:
                try:
                    spor_om_dato(cursor)
                except Exception as e:
                    print(f"ERROR: {e}")
                input("Trykk enter for å gå tilbake")
                break
            elif program == 5:
                try:
                    skuespillere_i_teaterstykker(cursor)
                except Exception as e:
                    print(f"ERROR: {e}")
                input("Trykk enter for å gå tilbake")
                break
            elif program == 6:
                try:
                    mest_solgt_forestilling(cursor)
                except Exception as e:
                    print(f"ERROR: {e}")
                input("Trykk enter for å gå tilbake")
                break
            elif program == 7:
                try:
                    skuespillere_i_samme_akt(cursor)
                except Exception as e:
                    print(f"ERROR: {e}")
                input("Trykk enter for å gå tilbake")
                break

if __name__ == "__main__":
    main()