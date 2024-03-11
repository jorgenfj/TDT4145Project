import sqlite3

con = sqlite3.connect('teater.db')

cursor = con.cursor()

file_path = '/home/jorgen/spring2024/datdat/TDT4145Project/hovedscenen.txt'
SalID = 1
BillettNr = 0
KjopID = 0 

def scan_seats_hovedscenen():
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        print("File not found.")
    
# file_contents = scan_seats_hovedscenen()


def get_date(file_contents):
    date = file_contents.split('\n')[0]
    date = date[5:]
    return date

def get_seats_galleri():
    RadNr = 0
    OmraadeNavn = "Galleri"
    seats = []
    for i in range (505, 525):
        seat = f"{SalID}, {RadNr}, {i}, '{OmraadeNavn}'"
        seats.append(seat)
    return seats

def get_seats_parkett():
    OmraadeNavn = "Parkett"
    seats = []
    for i in range (1, 19):
        for j in range (1, 29):
            if((i==17 or i==18) and 18 < j < 23):
                continue
            seat = f"{SalID}, {i}, {(i-1)*28 + j}, '{OmraadeNavn}'"
            seats.append(seat)
    return seats

def get_seats_hovedscenen():
    seats = []
    seats.extend(get_seats_galleri())
    seats.extend(get_seats_parkett())
    return seats

def insert_seats_hovedscenen(cursor):
    seats = get_seats_hovedscenen()
    for seat in seats:
        cursor.execute(f"INSERT INTO Stol VALUES ({seat})")


def insert_tickets_hovedscenen():
    file_contents = scan_seats_hovedscenen()
    lines = file_contents.split('\n')
    parkett_seats_lines = lines[7:]
    parkett_seats_lines = parkett_seats_lines[::-1]
    cursor.execute(f"INSERT INTO Teaterbillett VALUES ({KjopID}, 1)")
    
    for row, line in enumerate(parkett_seats_lines):
        for col, seat in enumerate(line.strip()):
            if seat == '1':
                seat_num = (row) * 28 + col + 1  
                reserved_seat = {"SalID": SalID, "RadNr": row, "SeteNr": seat_num, "OmraadeNavn": "Parkett"}
                insert_billett(reserved_seat)
    con.commit()


def insert_billett(seat):
    global BillettNr  
    BillettNr += 1
    
    try:
        cursor.execute(f"INSERT INTO Billettype VALUES ({KjopID}, {BillettNr}, 1)")
        cursor.execute("INSERT INTO ReservererStol (KjopID, BillettNr, SalID, RadNr, SeteNr, OmraadeNavn) VALUES (?, ?, ?, ?, ?, ?)",
                       (KjopID, BillettNr, seat["SalID"], seat["RadNr"], seat["SeteNr"], seat["OmraadeNavn"]))
    except sqlite3.Error as e:
        print("An error occurred:", e)

# Make sure you open the database connection and create a cursor before calling these functions
# And ensure the database connection is closed after operations are


