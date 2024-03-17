import sqlite3

con = sqlite3.connect("teater.db")
cursor = con.cursor()
cursor.execute("PRAGMA encoding = 'UTF-8';")

def main():
   print("Velkommen til teateret\n")

def login():

    while(True):
      print("Velg login eller registrer bruker \n")
      print("1 - Login\n")
      print("2 - Registrer bruker\n")
      valg = input()
      
      if(valg == '1'):
        mobilnummer = input("mobilnummer: \n")

        cursor.execute(f"SELECT EXISTS(SELECT 1 FROM KundeProfil WHERE Mobilnummer = {mobilnummer})")
        (bruker_eksisterer) = cursor.fetchone()[0]

        if((bruker_eksisterer)):
           break
          
        else:
           print("Bruker eksisterer ikke\n")

      elif(valg == '2'):
        mobilnummer = input("Mobilnummer: ")
        navn = input("Navn: ")
        adresse = input("Adresse: ")
        cursor.execute(f"INSERT INTO KundeProfil (Mobilnummer, Navn, Adresse) VALUES ('{mobilnummer}', '{navn}', '{adresse}')")
        con.commit()
        print("Bruker opprettet, vennligst logg inn")
      
      else:
          print("Velg et gyldig alternativ")