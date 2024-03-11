import sqlite3

con = sqlite3.connect('teater.db')

cursor = con.cursor()

cursor.execute("INSERT INTO Skuespiller VALUES (1,'Jørgen')")


cursor.execute("SELECT * FROM Skuespiller")

row = cursor.fetchall()
con.commit()
print(row)
con.close()