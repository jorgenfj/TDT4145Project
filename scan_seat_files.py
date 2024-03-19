## SKAL I KJØTTKVERNA

hovedscenen_id = 1
gamle_scene_id = 2
kjop_id_hovedscenen = 1
kjop_id_gamle_scene = 2
BillettNr = 0
gamle_scene_file = "gamle-scene.txt"
hovedscenen_file = "hovedscenen.txt"
hovedscenen_tid = '19:00:00'
gamle_scene_tid = '18:30:00'

def read_seats_file(file_path):
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

def get_seats_hovedscene_galleri():
    RadNr = 0
    OmraadeNavn = "Galleri"
    seats = []
    for i in range(505, 525):
        seat = {"SalID": hovedscenen_id, "RadNr": RadNr, "SeteNr": i, "OmraadeNavn": OmraadeNavn}
        seats.append(seat)
    return seats

def scan_parkett_hovedscenen(lines):
    seats = []
    tickets = []
    for row, line in enumerate(lines):
        for col, seat_status in enumerate(line.strip()):
            if seat_status == 'x':
                continue
            seat_num = (row) * 28 + col + 1  
            seat = {"SalID": hovedscenen_id, "RadNr": row+1, "SeteNr": seat_num, "OmraadeNavn": "Parkett"}
            seats.append(seat)
            if seat_status == '1':
                reserved_seat = {"SalID": hovedscenen_id, "RadNr": row+1, "SeteNr": seat_num, "OmraadeNavn": "Parkett"}
                tickets.append(reserved_seat)
    return seats, tickets


def scan_section_gamle_scene(section, galleri_section_rows):
    seats = []
    tickets = []
    for row, line in enumerate(galleri_section_rows):
        for seatNr, seat_status in enumerate(line.strip()):
            seat_num = seatNr + 1  
            seat = {"SalID": gamle_scene_id, "RadNr": row+1, "SeteNr": seatNr+1, "OmraadeNavn": section}
            seats.append(seat)
            if seat_status == '1':
                reserved_seat = {"SalID": gamle_scene_id, "RadNr": row+1, "SeteNr": seat_num, "OmraadeNavn": section}
                tickets.append(reserved_seat)
    return seats, tickets


def insert_seats(seats, cursor):
    for seat in seats:
        cursor.execute("INSERT INTO Stol (SalID, RadNr, SeteNr, OmraadeNavn) VALUES (?, ?, ?, ?)",
                       (seat["SalID"], seat["RadNr"], seat["SeteNr"], seat["OmraadeNavn"]))

def insert_tickets(tickets, cursor, KjopID):
    global BillettNr
    BillettNr = 0
    for ticket in tickets:
        BillettNr += 1
        cursor.execute(f"INSERT INTO Billettype VALUES ({KjopID}, {BillettNr}, 'ORDINAER')")
        cursor.execute("INSERT INTO ReservererStol (KjopID, BillettNr, SalID, RadNr, SeteNr, OmraadeNavn) VALUES (?, ?, ?, ?, ?, ?)",
                    (KjopID, BillettNr, ticket["SalID"], ticket["RadNr"], ticket["SeteNr"], ticket["OmraadeNavn"]))
        
def scan_seats_gamle_scene(cursor):
    seats, tickets = [], []

    # Read seats file
    file_contents = read_seats_file(gamle_scene_file)
    lines = file_contents.split('\n')
    lines = [line for line in lines if line.strip()]
    lines = lines[1:]  # Skip date line

     # Find section names and corresponding lines
    section_lines = {}
    current_section = None
    for line in lines:
        if line.isalpha():
            current_section = line
            section_lines[current_section] = []
        else:
            section_lines[current_section].append(line)

    # Process each section
    for section, section_lines in section_lines.items():
        section_lines = section_lines[::-1]  # Reverse lines for each section
        new_seats, new_tickets = scan_section_gamle_scene(section, section_lines)
        seats.extend(new_seats)
        tickets.extend(new_tickets)


    cursor.execute(f"INSERT INTO Billettkjop VALUES ({kjop_id_gamle_scene}, 2, 0, 0, 0)")
    cursor.execute(f"INSERT INTO Teaterbillett VALUES ({kjop_id_gamle_scene}, 2)")
    cursor.execute(f"INSERT INTO ReservererForestilling VALUES ({kjop_id_gamle_scene}, 2, '{get_date(file_contents)}', '{gamle_scene_tid}')") 

    insert_seats(seats, cursor)
    insert_tickets(tickets, cursor, kjop_id_gamle_scene)

def scan_seats_hovedscenen(cursor):
    seats, tickets = [], []
    # Read seats file
    file_contents = read_seats_file(hovedscenen_file)
    lines = file_contents.split('\n')
    lines = [line for line in lines if line.strip()]
    lines = lines[7:]  # Skip to lines in Parkett section

    seats.extend(get_seats_hovedscene_galleri())
    new_seats, new_tickets = scan_parkett_hovedscenen(lines)
    seats.extend(new_seats)
    tickets.extend(new_tickets)
    cursor.execute(f"INSERT INTO Billettkjop VALUES ({kjop_id_hovedscenen}, 1, 0, 0, 0)")
    cursor.execute(f"INSERT INTO Teaterbillett VALUES ({kjop_id_hovedscenen}, 1)")
    cursor.execute(f"INSERT INTO ReservererForestilling VALUES ({kjop_id_hovedscenen}, 1, '{get_date(file_contents)}', '{hovedscenen_tid}')") 

    insert_seats(seats, cursor)
    insert_tickets(tickets, cursor, kjop_id_hovedscenen)