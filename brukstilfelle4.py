from prettytable import PrettyTable, ALL
import re

def spor_om_dato(cursor):
    print("\nHer kan du søke etter forestillinger på en gitt dato")
    print("Skriv inn en dato på formen åååå-mm-dd")
    while(True):
        dato = input()
        if (dato == 'q'):
            break
        gyldig_dato = r'(2024-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|[3][01]))$'

        if not re.match(gyldig_dato, dato):
            print('\nVennligst skriv en gyldig dato for sesongen 2024 på formen åååå-mm-dd')
        else:
            sql_fil = open("brukstilfelle4.sql", 'r')
            sql_sporring = sql_fil.read()
            sql_fil.close()

            cursor.execute(sql_sporring, (dato,))
            forestillinger = cursor.fetchall()
            
            if(len(forestillinger) != 0):
                forestillinger_tabell = PrettyTable(['Forestillingsdato', 'Teaterstykke', 'Tidspunkt', 'Antall Solgte Billetter'])
                forestillinger_tabell.hrules = ALL
                forestillinger_tabell.add_rows(forestillinger)
                print(f'\n{forestillinger_tabell}\n')
                break
            
            else: 
                print(f'\nPå {dato} finnes det foreløpig ingen forestillinger, prøv en annen dato\n')
                break