from prettytable import PrettyTable, ALL
import sqlite3
import re

con = sqlite3.connect("teater.db")
cursor = con.cursor()
cursor.execute("PRAGMA encoding = 'UTF-8';")

def spor_om_dato():
    while(True):
        print("\nHer kan du søke etter forestillinger på en gitt dato")
        print("Skriv inn en dato på formen åååå-mm-dd")
        dato = input()
        gyldig_dato = r'(2024-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|[3][01]))$'

        if not re.match(gyldig_dato, dato):
            print('\n\nVennligst skriv en gyldig dato\n')
        else:
            cursor.execute(f'''
                           SELECT Dato, T.Tittel, Tidspunkt, COALESCE(COUNT(S.BillettNr), 0) 
                           FROM Forestilling AS F 
                           LEFT JOIN Teaterstykke as T ON F.TeaterstykkeID = T.TeaterstykkeID 
                           LEFT JOIN ReservererForestilling as R ON T.TeaterstykkeID = R.TeaterstykkeID 
                           AND F.Dato = R.ForestillingsDato 
                           LEFT JOIN ReservererStol as S ON R.KjopID = S.KjopID 
                           WHERE Dato IS "{dato}" 
                           GROUP BY T.TeaterstykkeID 
                           ORDER BY F.Tidspunkt''')
            forestillinger = cursor.fetchall()
            
            if(len(forestillinger) != 0):
                forestillinger_tabell = PrettyTable(['Forestillingsdato', 'Teaterstykke', 'Tidspunkt', 'Antall Solgte Billetter'])
                forestillinger_tabell.hrules = ALL
                forestillinger_tabell.add_rows(forestillinger)
                print(f'\n {forestillinger_tabell} \n')
                break
            
            else: 
                print(f'\nPå {dato} finnes det foreløpig ingen forestillinger\n\n')


spor_om_dato()
        
