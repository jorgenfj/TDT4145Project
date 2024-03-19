import sqlite3

def create_database_from_sql_script(db_file, sql_script_file):
    # Connect to the SQLite database (this will create the database if it doesn't exist)
    con = sqlite3.connect(db_file)
    cursor = con.cursor()
    
    # Read SQL script
    sql_fil = open(sql_script_file, 'r')
    sql_sporring = sql_fil.read()
    sql_fil.close()
    
    # Execute SQL script
    try:
        cursor.executescript(sql_sporring)
        con.commit()
        print(f"Database and tables created successfully from {sql_script_file}.")
    except sqlite3.Error as e:
        print(f"Error: {e.args[0]}")
    finally:
        con.close()
