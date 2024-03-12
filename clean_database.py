import sqlite3
from fill_database import fill_database

def create_database_from_sql_script(db_file, sql_script_file):
    # Connect to the SQLite database (this will create the database if it doesn't exist)
    con = sqlite3.connect(db_file)
    cursor = con.cursor()
    
    # Read SQL script
    with open(sql_script_file, 'r') as file:
        sql_script = file.read()
    
    # Execute SQL script
    try:
        # This executes the SQL script in one go if it does not require parsing
        cursor.executescript(sql_script)
        con.commit()
        print(f"Database and tables created successfully from {sql_script_file}.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e.args[0]}")
    finally:
        # Close the connection
        con.close()

# Specify your database file name and SQL script file name
db_file = 'teater.db'
sql_script_file = 'teater.sql'

# Create the database and tables
create_database_from_sql_script(db_file, sql_script_file)
fill_database()
