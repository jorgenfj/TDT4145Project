import sqlite3
# from scan_seats_hovedscenen import insert_seats_hovedscenen, insert_tickets_hovedscenen
# from scan_seats_gamle_scene import insert_seats_gamle_scene, insert_tickets_gamle_scene
from scan_seat_files import scan_seats_gamle_scene, scan_seats_hovedscenen


def fill_database():
  con = sqlite3.connect("teater.db")
  con.execute('PRAGMA foreign_keys = ON')
  cursor = con.cursor()
  cursor.execute("PRAGMA encoding = 'UTF-8';")

  # Stoler
  # insert_seats_hovedscenen(cursor)
  # insert_seats_gamle_scene(cursor)

  # Billetter
  # insert_tickets_hovedscenen(cursor)
  # insert_tickets_gamle_scene(cursor)
 
  scan_seats_hovedscenen(cursor)
  scan_seats_gamle_scene(cursor)
  
  con.commit()