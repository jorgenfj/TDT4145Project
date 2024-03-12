file_path = 'gamle-scene.txt'
SalID = 2
KjopID = 1
BillettNr = 0
tid = '18:30:00'

def read_seats_file_gamle_scene():
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        print("File not found.")

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
    seats.extend(get_seats_balkong())
    seats.extend(get_seats_parkett())
    return seats

def insert_seats_gamle_scene(cursor):
    seats = get_seats_gamle_scene()
    for seat in seats:
        cursor.execute(f"INSERT INTO Stol VALUES ({seat})")

def insert_tickets_gamle_scene(cursor):
    file_contents = read_seats_file_gamle_scene()
    lines = file_contents.split('\n')
    lines = [line for line in lines if line.strip()]
    tickets = []
    galleri_seats_lines = lines[2:5]
    galleri_seats_lines = galleri_seats_lines[::-1]
    balkong_seats_lines = lines[6:10]
    balkong_seats_lines = balkong_seats_lines[::-1]
    parkett_seats_lines = lines[11:21]
    parkett_seats_lines = parkett_seats_lines[::-1]
    tickets.extend(get_tickets_gamle_scene_galleri("Galleri", galleri_seats_lines))
    tickets.extend(get_tickets_gamle_scene_balkong("Balkong", balkong_seats_lines))
    tickets.extend(get_tickets_gamle_scene_parkett("Parkett", parkett_seats_lines))

    cursor.execute(f"INSERT INTO Billettkjop VALUES ({KjopID}, 1, 0, 0, 0)")
    cursor.execute(f"INSERT INTO Teaterbillett VALUES ({KjopID}, 1)")
    cursor.execute(f"INSERT INTO ReservererForestilling VALUES ({KjopID}, 2, '{get_date(file_contents)}', '{tid}')") 

    insert_tickets(tickets, cursor)
 

def get_tickets_gamle_scene_galleri(section, galleri_seats_lines):
    tickets = []
    for row, line in enumerate(galleri_seats_lines):
        for col, seat in enumerate(line.strip()):
            if seat == '1':
                seat_num = col + 1  
                reserved_seat = {"SalID": SalID, "RadNr": row+1, "SeteNr": seat_num, "OmraadeNavn": section}
                tickets.append(reserved_seat)
    return tickets

def scan_seats_gamle_scene(section, galleri_seats_lines):
    seats = []
    tickets = []
    for row, line in enumerate(galleri_seats_lines):
        for seatNr, seat_status in enumerate(line.strip()):
            seat_num = seatNr + 1  
            seat = {"SalID": SalID, "RadNr": row+1, "SeteNr": seatNr+1, "OmraadeNavn": section}
            if seat_status == '1':
                reserved_seat = {"SalID": SalID, "RadNr": row+1, "SeteNr": seat_num, "OmraadeNavn": section}
                tickets.append(reserved_seat)
    return seats, tickets
    
                
def get_tickets_gamle_scene_balkong(section, galleri_seats_lines):
    tickets = []
    for row, line in enumerate(galleri_seats_lines):
        for col, seat in enumerate(line.strip()):
            if seat == '1':
                seat_num = col + 1  
                reserved_seat = {"SalID": SalID, "RadNr": row+1, "SeteNr": seat_num, "OmraadeNavn": section}
                tickets.append(reserved_seat)
    return tickets

def get_tickets_gamle_scene_parkett(section, galleri_seats_lines):
    tickets = []
    for row, line in enumerate(galleri_seats_lines):
        for col, seat in enumerate(line.strip()):
            if seat == '1':
                seat_num = col + 1  
                reserved_seat = {"SalID": SalID, "RadNr": row+1, "SeteNr": seat_num, "OmraadeNavn": section}
                tickets.append(reserved_seat)
    return tickets

def insert_tickets(tickets, cursor):
    for ticket in tickets:
        global BillettNr  
        BillettNr += 1
        cursor.execute(f"INSERT INTO Billettype VALUES ({KjopID}, {BillettNr}, 'ORDINAER')")
        cursor.execute("INSERT INTO ReservererStol (KjopID, BillettNr, SalID, RadNr, SeteNr, OmraadeNavn) VALUES (?, ?, ?, ?, ?, ?)",
                    (KjopID, BillettNr, ticket["SalID"], ticket["RadNr"], ticket["SeteNr"], ticket["OmraadeNavn"]))
