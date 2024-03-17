from prettytable import PrettyTable, ALL
import sqlite3

con = sqlite3.connect("teater.db")
cursor = con.cursor()
cursor.execute("PRAGMA encoding = 'UTF-8';")

def mest_solgt_forestilling():
    cursor.execute(f'''
                   SELECT T.Tittel, F.Dato, COUNT(S.BillettNr) AS SolgtePlasser 
                   FROM Forestilling AS F 
                   LEFT JOIN Teaterstykke as T ON F.TeaterstykkeID = T.TeaterstykkeID 
                   LEFT JOIN ReservererForestilling as R ON T.TeaterstykkeID = R.TeaterstykkeID 
                   AND F.Dato = R.ForestillingsDato 
                   LEFT JOIN ReservererStol as S ON R.KjopID = S.KjopID 
                   GROUP BY T.TeaterstykkeID, F.Dato 
                   ORDER BY SolgtePlasser DESC''')
    #dersom man bytter LEFT til INNER får man kun forestillinger som har solgt minst 1 billett
    forestillinger = cursor.fetchall()
    if(len(forestillinger) != 0):
        forestillinger_tabell = PrettyTable(['Tittel', 'Dato', 'Solgte Plasser'])
        # forestillinger_tabell.hrules = ALL
        forestillinger_tabell.add_rows(forestillinger)
        print(f'\n{forestillinger_tabell}\n')
    else:
        print('Det finnes ingen forestillinger å vise')

# mest_solgt_forestilling()