import sqlite3
from clean_database import create_database_from_sql_script, fill_database
from scan_seat_files import scan_seats_hovedscenen, scan_seats_gamle_scene

db_file = 'teater.db'
sql_script_file = 'teater.sql'

con = sqlite3.connect(db_file)
cursor = con.cursor()
con.execute('PRAGMA foreign_keys = ON')
cursor.execute("PRAGMA encoding = 'UTF-8';")

def main():
    create_database_from_sql_script(db_file, sql_script_file)
    #fyll_database()
    scan_seats_hovedscenen(cursor)
    scan_seats_gamle_scene(cursor)
    print('\nVelkommen til Trøndelag Teater!\n')
    print('Du har nå _ valg, trykk tallet som korresponderer til ønsket handling:')
    print('''
          1 - Søk på forestilling etter dato
          2 - ''')

    

