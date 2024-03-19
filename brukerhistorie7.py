from prettytable import PrettyTable

def brukerhistorie7(cursor):
    skuespiller_navn = input("Skriv inn navnet på skuespilleren du vil ha informasjon om: ")

    sql_fil = open("brukerhistorie7.sql", 'r')
    sql_sporring = sql_fil.read()
    sql_fil.close()

    cursor.execute(sql_sporring, (skuespiller_navn,))
    medskuespillere = cursor.fetchall()

    tabell = PrettyTable(['Teaterstykke', 'Skuespiller', 'Co-Skuespiller'])
    for rad in medskuespillere:
        tabell.add_row(rad)
    print(tabell)