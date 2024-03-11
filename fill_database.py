import sqlite3
from scan_seats_hovedscenen import insert_seats_hovedscenen
from scan_seats_gamle_scene import insert_seats_gamle_scene

def fill_database():
  con = sqlite3.connect("teater.db")
  cursor = con.cursor()
#   cursor.execute("""PRAGMA encoding = "UTF-8" """)

  # Teatersaler
  cursor.execute("INSERT INTO Teatersal VALUES (1, 'Hovedscenen', 520)")
  cursor.execute("INSERT INTO Teatersal VALUES (2, 'Gamle Scene', 332)")

  # Teaterstykker
  cursor.execute("INSERT INTO Teaterstykke VALUES (1, 'Kongsemnene', 'Henrik Ibsen', 1)")
  cursor.execute("INSERT INTO Teaterstykke VALUES (2, 'Størst av alt er kjærligheten', 'Jonas Corell Petersen', 2)")

  # Akter
  # Kongsemnene
  cursor.execute("INSERT INTO Akt VALUES (1, 1, '')")
  cursor.execute("INSERT INTO Akt VALUES (1, 2, '')")
  cursor.execute("INSERT INTO Akt VALUES (1, 3, '')")
  cursor.execute("INSERT INTO Akt VALUES (1, 4, '')")
  cursor.execute("INSERT INTO Akt VALUES (1, 5, '')")
  
  # Størst av alt er kjærligheten
  cursor.execute("INSERT INTO Akt VALUES (2, 1, '')")

  # Skuespillere
  # Kongsemnene
  cursor.execute("INSERT INTO Skuespiller VALUES (1, 'Arturo Scotti')")
  cursor.execute("INSERT INTO Skuespiller VALUES (2, 'Ingunn Beate Strige Øyen')")
  cursor.execute("INSERT INTO Skuespiller VALUES (3, 'Hans Petter Nilsen')")
  cursor.execute("INSERT INTO Skuespiller VALUES (4, 'Madeline Brandtzæg Nilsen')")
  cursor.execute("INSERT INTO Skuespiller VALUES (5, 'Synnøve Fossum Eriksen')")
  cursor.execute("INSERT INTO Skuespiller VALUES (6, 'Emma Caroline Deichmann')")
  cursor.execute("INSERT INTO Skuespiller VALUES (7, 'Thomas Jensen Takyi')")
  cursor.execute("INSERT INTO Skuespiller VALUES (8, 'Per Bogstad Gulliksen')")
  cursor.execute("INSERT INTO Skuespiller VALUES (9, 'Isak Holmen Sørensen')")
  cursor.execute("INSERT INTO Skuespiller VALUES (10, 'Fabian Heidelberg Lunde')")
  cursor.execute("INSERT INTO Skuespiller VALUES (11, 'Emil Olafsson')")
  cursor.execute("INSERT INTO Skuespiller VALUES (12, 'Snorre Ryen Tøndel')")

  # Størst av alt er kjærligheten
  cursor.execute("INSERT INTO Skuespiller VALUES (13, 'Sunniva Du Mond Nordal')")
  cursor.execute("INSERT INTO Skuespiller VALUES (14, 'Jo Saberniak')")
  cursor.execute("INSERT INTO Skuespiller VALUES (15, 'Marte M. Steinholt')")
  cursor.execute("INSERT INTO Skuespiller VALUES (16, 'Tor Ivar Hagen')")
  cursor.execute("INSERT INTO Skuespiller VALUES (17, 'Trond-Ove Skrødal')")
  cursor.execute("INSERT INTO Skuespiller VALUES (18, 'Natalie Grøndahl Tangen')")
  cursor.execute("INSERT INTO Skuespiller VALUES (19, 'Åsmund Flaten')")

  # Roller
  # Kongsemnene
  cursor.execute("INSERT INTO Rolle VALUES (1, 'Haakon Haakonssønn')")
  cursor.execute("INSERT INTO Rolle VALUES (2, 'Dagfinn Bonde')")
  cursor.execute("INSERT INTO Rolle VALUES (3, 'Jatgeir Skald')")
  cursor.execute("INSERT INTO Rolle VALUES (4, 'Sigrid')")
  cursor.execute("INSERT INTO Rolle VALUES (5, 'Ingebjørg')")
  cursor.execute("INSERT INTO Rolle VALUES (6, 'Baard Bratte')")
  cursor.execute("INSERT INTO Rolle VALUES (7, 'Skule Jarl')")
  cursor.execute("INSERT INTO Rolle VALUES (8, 'Inga frå Vartejg')")
  cursor.execute("INSERT INTO Rolle VALUES (9, 'Paal Flida')")
  cursor.execute("INSERT INTO Rolle VALUES (10, 'Ragnhild')")
  cursor.execute("INSERT INTO Rolle VALUES (11, 'Gregorius Jonssønn')")
  cursor.execute("INSERT INTO Rolle VALUES (12, 'Margrete')")
  cursor.execute("INSERT INTO Rolle VALUES (13, 'Biskop Nikolas')")
  cursor.execute("INSERT INTO Rolle VALUES (14, 'Peter')")

  # Størst av alt er kjærligheten
  cursor.execute("INSERT INTO Rolle VALUES (15, 'Sunniva Du Mond Nordal')")
  cursor.execute("INSERT INTO Rolle VALUES (16, 'Jo Saberniak')")
  cursor.execute("INSERT INTO Rolle VALUES (17, 'Marte M. Steinholt')")
  cursor.execute("INSERT INTO Rolle VALUES (18, 'Tor Ivar Hagen')")
  cursor.execute("INSERT INTO Rolle VALUES (19, 'Trond-Ove Skrødal')")
  cursor.execute("INSERT INTO Rolle VALUES (20, 'Natalie Grøndahl Tangen')")
  cursor.execute("INSERT INTO Rolle VALUES (21, 'Åsmund Flaten')")

  # Spilles av
  cursor.execute("INSERT INTO SpillesAv VALUES (1, 1)")
  cursor.execute("INSERT INTO SpillesAv VALUES (2, 8)")
  cursor.execute("INSERT INTO SpillesAv VALUES (3, 7)")
  cursor.execute("INSERT INTO SpillesAv VALUES (4, 10)")
  cursor.execute("INSERT INTO SpillesAv VALUES (5, 12)")
  cursor.execute("INSERT INTO SpillesAv VALUES (6, 4)")
  cursor.execute("INSERT INTO SpillesAv VALUES (6, 5)")
  cursor.execute("INSERT INTO SpillesAv VALUES (7, 13)")
  cursor.execute("INSERT INTO SpillesAv VALUES (8, 11)")
  cursor.execute("INSERT INTO SpillesAv VALUES (10, 6)")
  cursor.execute("INSERT INTO SpillesAv VALUES (11, 3)")
  cursor.execute("INSERT INTO SpillesAv VALUES (11, 2)")
  cursor.execute("INSERT INTO SpillesAv VALUES (12, 14)")

  # Størst av alt er kjærligheten
  cursor.execute("INSERT INTO SpillesAv VALUES (13, 15)")
  cursor.execute("INSERT INTO SpillesAv VALUES (14, 16)")
  cursor.execute("INSERT INTO SpillesAv VALUES (15, 17)")
  cursor.execute("INSERT INTO SpillesAv VALUES (16, 18)")
  cursor.execute("INSERT INTO SpillesAv VALUES (17, 19)")
  cursor.execute("INSERT INTO SpillesAv VALUES (18, 20)")
  cursor.execute("INSERT INTO SpillesAv VALUES (19, 21)")

  # SpillesIAkt
  # Kongsemnene
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 1, 1)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 2, 1)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 3, 1)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 4, 1)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 5, 1)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 1, 2)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 2, 2)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 3, 2)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 4, 2)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 5, 2)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 4, 3)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 1, 4)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 2, 4)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 5, 4)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 4, 5)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 1, 6)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 1, 7)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 2, 7)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 3, 7)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 4, 7)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 5, 7)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 1, 8)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 3, 8)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 1, 9)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 2, 9)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 3, 9)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 4, 9)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 5, 9)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 1, 10)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 5, 10)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 1, 11)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 2, 11)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 3, 11)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 4, 11)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 5, 11)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 1, 12)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 2, 12)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 3, 12)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 4, 12)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 5, 12)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 1, 13)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 2, 13)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 3, 13)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 3, 14)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 4, 14)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (1, 5, 14)")

  # Størst av alt er kjærligheten
  cursor.execute("INSERT INTO SpillesIAkt VALUES (2, 1, 15)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (2, 1, 16)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (2, 1, 17)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (2, 1, 18)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (2, 1, 19)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (2, 1, 20)")
  cursor.execute("INSERT INTO SpillesIAkt VALUES (2, 1, 21)")

  # Forestillinger
  # Kongsemnene
  cursor.execute("INSERT INTO Forestilling VALUES (1, '2024-02-01', '19:00:00')")
  cursor.execute("INSERT INTO Forestilling VALUES (1, '2024-02-02', '19:00:00')")
  cursor.execute("INSERT INTO Forestilling VALUES (1, '2024-02-03', '19:00:00')")
  cursor.execute("INSERT INTO Forestilling VALUES (1, '2024-02-05', '19:00:00')")
  cursor.execute("INSERT INTO Forestilling VALUES (1, '2024-02-06', '19:00:00')")

  # Størst av alt er kjærligheten
  cursor.execute("INSERT INTO Forestilling VALUES (2, '2024-02-06', '18:30:00')")
  cursor.execute("INSERT INTO Forestilling VALUES (2, '2024-02-07', '18:30:00')")
  cursor.execute("INSERT INTO Forestilling VALUES (2, '2024-02-03', '18:30:00')")
  cursor.execute("INSERT INTO Forestilling VALUES (2, '2024-02-12', '18:30:00')")
  cursor.execute("INSERT INTO Forestilling VALUES (2, '2024-02-13', '18:30:00')")
  cursor.execute("INSERT INTO Forestilling VALUES (2, '2024-02-14', '18:30:00')")

  # Pristyper
  # Kongsemnene
  cursor.execute("INSERT INTO Pristyper VALUES (1, 'ORDINAER', 450)")
  cursor.execute("INSERT INTO Pristyper VALUES (1, 'HONNOR', 380)")
  cursor.execute("INSERT INTO Pristyper VALUES (1, 'STUDENT', 280)")

  # Størst av alt er kjærligheten
  cursor.execute("INSERT INTO Pristyper VALUES (2, 'ORDINAER', 350)")
  cursor.execute("INSERT INTO Pristyper VALUES (2, 'HONNOR', 300)")
  cursor.execute("INSERT INTO Pristyper VALUES (2, 'STUDENT', 220)")
  cursor.execute("INSERT INTO Pristyper VALUES (2, 'BARN', 220)")

  # Stoler
  insert_seats_hovedscenen(cursor)
  insert_seats_gamle_scene(cursor)


  # Kundeprofiler
  cursor.execute("INSERT INTO KundeProfil VALUES (0, 99999999, 'Testbruker', 'Testveien 1')")

  # Involverte
  # Kongsemnene
  cursor.execute("INSERT INTO Involvert VALUES (1, 'Yury Butusov', 'yury@gmail.com', 'fast ansatt')")
  cursor.execute("INSERT INTO Involvert VALUES (2, 'Aleksandr Shishkin-Hokusai', 'aleksandr@gmail.com', 'fast ansatt')")
  cursor.execute("INSERT INTO Involvert VALUES (3, 'Eivind Myren', 'eivind@gmail.com', 'fast ansatt')")
  cursor.execute("INSERT INTO Involvert VALUES (4, 'Mina Rype Stokke', 'mina@gmail.com', 'fast ansatt')")

  # Størst av alt er kjærligheten
  cursor.execute("INSERT INTO Involvert VALUES (5, 'Jonas Corell Petersen', 'jonas@gmail.com', 'fast ansatt')")
  cursor.execute("INSERT INTO Involvert VALUES (6, 'David Gehrt', 'david@gmail.com', 'fast ansatt')")
  cursor.execute("INSERT INTO Involvert VALUES (7, 'Gaute Tønder', 'gaute@gmail.com', 'fast ansatt')")
  cursor.execute("INSERT INTO Involvert VALUES (8, 'Magnus Mikaelsen', 'magnus@gmail.com', 'fast ansatt')")
  cursor.execute("INSERT INTO Involvert VALUES (9, 'Kristoffer Spender', 'kristoff@gmail.com', 'fast ansatt')")

  # Oppgaver
  # Kongsemnene
  cursor.execute("INSERT INTO Oppgave VALUES (1, 'Regi og musikkutvelgelse', 'Regissør og ansvarlig for utvalgt muskk for Kongsemnene', 1)")
  cursor.execute("INSERT INTO Oppgave VALUES (3, 'Scenografi og kostymer', 'Scene og kostymer for Kongsemnene', 1)")
  cursor.execute("INSERT INTO Oppgave VALUES (2, 'Lysdesign', 'Design av lys for Kongsemnene', 1)")
  cursor.execute("INSERT INTO Oppgave VALUES (4, 'Dramaturg', 'Ansvar for drama for Kongsemnene', 1)")

  # Størst av alt er kjærligheten
  cursor.execute("INSERT INTO Oppgave VALUES (5, 'Regi', 'Regissering av stykket for Størst av alt er kjærligheten', 2)")
  cursor.execute("INSERT INTO Oppgave VALUES (6, 'Scenografi og kostymer', 'Scene og kostymer for Størst av alt er kjærligheten', 2)")
  cursor.execute("INSERT INTO Oppgave VALUES (7, 'Musikalsk ansvarlig', 'Ansvarlig for musikk for Størst av alt er kjærligheten', 2)")
  cursor.execute("INSERT INTO Oppgave VALUES (8, 'Lysdesign', 'Design av ly for Størst av alt er kjærlighetens', 2)")
  cursor.execute("INSERT INTO Oppgave VALUES (9, 'Dramaturg', 'Ansvar for drama for Størst av alt er kjærligheten', 2)")

  # Oppgav_er utføres av
  # Kongsemnene
  cursor.execute("INSERT INTO UtforesAv VALUES (1, 1)")
  cursor.execute("INSERT INTO UtforesAv VALUES (2, 2)")
  cursor.execute("INSERT INTO UtforesAv VALUES (3, 3)")
  cursor.execute("INSERT INTO UtforesAv VALUES (4, 4)")

  # Størst av alt er kjærligheten
  cursor.execute("INSERT INTO UtforesAv VALUES (5, 5)")
  cursor.execute("INSERT INTO UtforesAv VALUES (6, 6)")
  cursor.execute("INSERT INTO UtforesAv VALUES (7, 7)")
  cursor.execute("INSERT INTO UtforesAv VALUES (8, 8)")
  cursor.execute("INSERT INTO UtforesAv VALUES (9, 9)")
  
  con.commit()
# fill_database()