import sqlite3

con = sqlite3.connect('teater.db')

cursor = con.cursor()

file_path = '/home/jorgen/spring2024/datdat/TDT4145Project/gamle-scenen.txt'
SalID = 2

def scan_seats_gamle_scene():
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        print("File not found.")
    
# file_contents = scan_seats_gamle_scene()


def get_date(file_contents):
    date = file_contents.split('\n')[0]
    date = date[5:]
    return date

def get_seats_galleri():
    OmraadeNavn = "Galleri"
    seats = []
    for i in range (1, 4):
        for j in range (1, 34):
            if((i == 2 and j > 18) or (i == 3 and j > 17)):
                continue
            seat = f"{SalID}, {i}, {j}, '{OmraadeNavn}'"
            seats.append(seat)
    return seats

def get_seats_balkong():
    OmraadeNavn = "Balkong"
    seats = []
    for i in range (1, 5):
        for j in range (1, 29):
            if((i == 2 and j > 27)
               or (i == 3 and j > 22)
               or i == 4 and j > 17):
                continue
            seat = f"{SalID}, {i}, {j}, '{OmraadeNavn}'"
            seats.append(seat)
    return seats


def get_seats_parkett():
    OmraadeNavn = "Parkett"
    seats = []
    for i in range (1, 11):
        for j in range (1, 19):
            if((i == 2 and j > 16)
               or (i in [3, 6, 8, 9] and j > 17)
               or i == 10 and j > 14):
                continue
            seat = f"{SalID}, {i}, {j}, '{OmraadeNavn}'"
            seats.append(seat)
    return seats

def get_seats_gamle_scene():
    seats = []
    seats.extend(get_seats_galleri())
    seats.extend(get_seats_parkett())
    return seats

def insert_seats_gamle_scene(cursor):
    seats = get_seats_gamle_scene()
    for seat in seats:
        cursor.execute(f"INSERT INTO Stol VALUES ({seat})")

# def read_sold_tickets():
#     file_contents_by_line = file_contents.split("\n")
#     for soldSeats in file_contents_by_line:
#         if soldSeats == 1:
#             return