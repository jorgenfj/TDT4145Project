def lag_tabeller_teater(sql_script_fil, cursor):
    # Koble til SQlLite databasen, dette lager en database om den ikke eksisterer.
    # Om en database eksisterer fra før vil den eksisterende bli slettet!
    
    # Les SQL script
    sql_fil = open(sql_script_fil, 'r')
    sql_sporring = sql_fil.read()
    sql_fil.close()
    cursor.executescript(sql_sporring)
