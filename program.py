from prettytable import PrettyTable
import sqlite3

con = sqlite3.connect("teater.db")
cursor = con.cursor()

def login():

    while(True):
      print("Velg login eller registrer bruker \n")
      print("1 - Login\n")
      print("2 - Registrer bruker\n")
      choice = input()
      
      if(choice == '1'):
        mobilnummer = input("mobilnummer: \n")

        cursor.execute(f"SELECT EXISTS(SELECT 1 FROM KundeProfil WHERE Mobilnummer = {mobilnummer})")
        existsBool = cursor.fetchone()
        print(existsBool)

        if(existsBool):
           break
          
        else:
           print("Bruker eksisterer ikke\n")

      elif(choice == '2'):
        mobilnummer = input("Mobilnummer: ")
        navn = input("Navn: ")
        adresse = input("Adresse: ")
        cursor.execute(f"INSERT INTO KundeProfil(Mobilnummer, Navn, Adresse) VALUES ('{mobilnummer}', '{navn}', '{adresse}')")
        con.commit()
        print("Bruker opprettet, vennligst logg inn")
      
      else:
          print("Velg et gyldig alternativ")

login()