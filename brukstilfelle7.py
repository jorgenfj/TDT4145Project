from prettytable import PrettyTable, ALL

def skuespillere_i_samme_akt(cursor):
    skuespiller_navn = input("Skriv inn navnet på skuespilleren du vil ha informasjon om: ")

    sql_fil = open("brukstilfelle7.sql", 'r')
    sql_sporring = sql_fil.read()
    sql_fil.close()

    cursor.execute(sql_sporring, (skuespiller_navn,))
    medskuespillere = cursor.fetchall()

    if(len(medskuespillere) != 0):
        medskuespillere_tabell = PrettyTable(['Teaterstykke', 'Skuespiller', 'Co-Skuespiller'])
        medskuespillere_tabell.hrules = ALL
        medskuespillere_tabell.add_rows(medskuespillere)
        print(f'\n{medskuespillere_tabell}\n')
    else:
        print('Det finnes ingen skuespillere å vise')