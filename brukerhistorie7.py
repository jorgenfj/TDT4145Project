from prettytable import PrettyTable
import sqlite3

con = sqlite3.connect("teater.db")
cursor = con.cursor()
cursor.execute("PRAGMA encoding = 'UTF-8';")

skuespiller_navn = input("Skriv inn navnet på skuespilleren du vil ha informasjon om: ")

with open("brukerhistorie7.sql", 'r') as sql_fil:
    sql_sporring = sql_fil.read()

cursor.execute(sql_sporring, (skuespiller_navn,))
medskuespillere = cursor.fetchall()

tabell = PrettyTable(['Teaterstykke', 'Skuespiller', 'Co-Skuespiller'])
for rad in medskuespillere:
    tabell.add_row(rad)
print(tabell)

cursor.close()
con.close()