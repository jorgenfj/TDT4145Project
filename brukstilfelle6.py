from prettytable import PrettyTable, ALL

def mest_solgt_forestilling(cursor):

    sql_fil = open("brukstilfelle6.sql", 'r')
    sql_sporring = sql_fil.read()
    sql_fil.close()

    cursor.execute(sql_sporring)
    forestillinger = cursor.fetchall()

    if(len(forestillinger) != 0):
        forestillinger_tabell = PrettyTable(['Tittel', 'Dato', 'Solgte Plasser'])
        forestillinger_tabell.hrules = ALL
        forestillinger_tabell.add_rows(forestillinger)
        print(f'\n{forestillinger_tabell}\n')
    else:
        print('Det finnes ingen forestillinger å vise')