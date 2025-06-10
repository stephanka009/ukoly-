from data import zvirata 
from evidence import pridejZvire, vypisZvirata 

def menu():
    while True: 
        print("\n--- Veterinární centrum ---")
        print("1. pridej zvire")
        print("2. vypsat vsechny zvirata")
        print("3. ukoncit")
        volba = input("Zadej volbu: ")

        if volba == "1":
            jmeno = input("Zadej jmeno zvirete: ")
            druh = input("Zadej druh zvkirete: ")
            pridejZvire(zvirata, jmeno, druh)
        elif volba == "2":
            vypisZvirata(zvirata)
        elif volba == "3":
         print("Program ukončen")
         
        else:
            print("Neplatna volba, zkuste to znovu")
            break

menu()
