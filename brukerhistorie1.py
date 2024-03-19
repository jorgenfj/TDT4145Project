import sqlite3
# from scan_seats_hovedscenen import insert_seats_hovedscenen, insert_tickets_hovedscenen
# from scan_seats_gamle_scene import insert_seats_gamle_scene, insert_tickets_gamle_scene
from scan_seat_files import scan_seats_gamle_scene, scan_seats_hovedscenen

def fill_database():
  con = sqlite3.connect("teater.db")
  con.execute('PRAGMA foreign_keys = ON')
  cursor = con.cursor()
  cursor.execute("PRAGMA encoding = 'UTF-8';")

  try:
    sql_fil = open("brukerhistorie1.sql", 'r')
    sql_sporring = sql_fil.read()
    sql_fil.close()

    cursor.executescript(sql_sporring)

    #Scanner seter fra .txt filer og legger de inn i databasen
    #Velger å gjøre dette i brukerhistorie1, og ikke brukerhistorie2
    scan_seats_hovedscenen(cursor)
    scan_seats_gamle_scene(cursor)
  except sqlite3.Error as e:
    print(f"An error occurred: {e.args[0]}")
  finally:
    con.commit()
    cursor.close()
    con.close()
    
fill_database()