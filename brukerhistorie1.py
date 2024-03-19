import sqlite3
from les_stoler import insett_stoler_fra_filer

def fyll_database(cursor):
  try:
    sql_fil = open("brukerhistorie1.sql", 'r')
    sql_sporring = sql_fil.read()
    sql_fil.close()

    cursor.executescript(sql_sporring)

    #Scanner seter fra .txt filer og legger de inn i databasen
    #Velger å gjøre dette i brukerhistorie1, og ikke brukerhistorie2
    insett_stoler_fra_filer(cursor)
    
  except sqlite3.Error as e:
    print(f"Error: {e.args[0]}")