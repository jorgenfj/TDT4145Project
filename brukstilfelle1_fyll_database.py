def fyll_database(cursor):
    sql_fil = open("brukstilfelle1.sql", 'r')
    sql_sporring = sql_fil.read()
    sql_fil.close()
    cursor.executescript(sql_sporring)