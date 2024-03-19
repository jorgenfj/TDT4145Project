import sqlite3
from clean_database import create_database_from_sql_script
from brukerhistorie1 import fyll_database
from brukerhistorie2 import insett_billetter_fra_filer
from billettkjop import billettkjop_system
from brukerhistorie4 import spor_om_dato
from brukerhistorie7 import brukerhistorie7

import re

db_file = 'teater.db'
sql_script_file = 'teater.sql'

con = sqlite3.connect(db_file)
cursor = con.cursor()
con.execute('PRAGMA foreign_keys = ON')
cursor.execute("PRAGMA encoding = 'UTF-8'")

def main():
    program = 0
    print('\nVelkommen til Trøndelag Teater!\n')
    while True:
        print('Du har 8 valg, trykk tallet som korresponderer til ønsket handling:')
        print('''
1 - Brukerhistoriene 1: Fyll databaser
2 - Brukerhistoriene 2: Legg inn seter fra gitt .txt filer
3 - Brukerhistoriene 3: Kjøp 9 billetter til Størst av alt er kjærligheten
4 - Brukerhistoriene 4: Søk på forestilling etter dato
5 - Brukerhistoriene 5: Navn på skuespillere i forskjellige teaterstykker
6 - Brukerhistoriene 6: Best solgt forestilling
7 - Brukerhistoriene 7: Skuespiller som har spilt med i samme akt
8 - Nullstill databasen
              ''')
        while True:
            program = input('Tast inn et tall: ')
            gyldig_program = r'[1-8]'
            if re.match(program, gyldig_program):
                print('Skriv inn et gyldig tall fra 1-7')
            else:
                program = int(program)
                break
        while True:
            if program == 1:
                create_database_from_sql_script(db_file, sql_script_file) # Burde kjøres på starten av main før første while loop?
                fyll_database(cursor)  # Får ikke lest inn stolene fra filene, mistenker cursor feil
                insett_stoler_fra_filer(cursor)
                print('Databasen er nå fylt')
                break
            elif program == 2:
                insett_billetter_fra_filer(cursor) #samme som over, får ikke lest inn billetter fordi vi mangler stoler
                print('Billettene er lest fra fil')
                break
            elif program == 3:  # begin transaction og rollback for hver brukerhistorie eller bare de som innsetter? Her i main eller i funksjonene?
                billettkjop_system(cursor)
                break
            elif program == 4:
                spor_om_dato(cursor)
                break
            elif program == 5:
                bh5 = open('brukerhistorie5.sql', 'r')
                brukerhistorie5 = bh5.read()
                bh5.close()
                con.execute(brukerhistorie5) # Tror python klager på "." i sql scriptet
                break
            elif program == 6:
                bh6 = open('brukerhistorie6.sql', 'r')
                brukerhistorie6 = bh6.read()
                bh6.close()
                con.execute(brukerhistorie6) # Tror python klager på "." i sql scriptet
                break
            elif program == 7:
                brukerhistorie7(cursor)
                break
            elif program == 8:
                create_database_from_sql_script(db_file, sql_script_file)
                break

if __name__ == "__main__":
    main()