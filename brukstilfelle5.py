from prettytable import PrettyTable, ALL

def skuespillere_i_teaterstykker(cursor):
    
    sql_fil = open("brukstilfelle5.sql", 'r')
    sql_sporring = sql_fil.read()
    sql_fil.close()

    cursor.execute(sql_sporring)
    forestillinger = cursor.fetchall()
    
    if(len(forestillinger) != 0):
        forestillinger_tabell = PrettyTable(['Teaterstykke', 'Skuespiller', 'Rolle'])
        forestillinger_tabell.hrules = ALL
        forestillinger_tabell.add_rows(forestillinger)
        print(f'\n{forestillinger_tabell}\n')
    else:
        print('Det finnes ingen skuespillere å vise')
