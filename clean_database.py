import sqlite3
from fill_database import fill_database
from scan_seats_hovedscenen import insert_tickets_hovedscenen

db_path = 'teater.db'
con = sqlite3.connect(db_path)
cursor = con.cursor()
tables = ['Teatersal', 'Teaterstykke', 'Forestilling', 'Pristyper', 'Stol', 'ReservererForestilling', 
          'ReservererStol', 'Teaterbillett', 'Billettype', 'Billettkjop', 'KundeProfil', 'Involvert', 
          'Oppgave', 'UtforesAv', 'Skuespiller', 'Rolle', 'SpillesAv', 'Akt', 'SpillesIAkt']
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()
# stripped_tables = [table[2:-3] for table in tables]
# print(tables)
    
def delete_records_from_tables(db_path, tables):
    try:
        for table in tables:
            cursor.execute(f"DELETE FROM {table};")
        con.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        con.close()


delete_records_from_tables(db_path, tables)
fill_database()
insert_tickets_hovedscenen()