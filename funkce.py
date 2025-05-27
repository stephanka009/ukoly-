# ukol 1 
def nasobek(cislo):
    vysledek = cislo * 5 
    print(vysledek)
nasobek(4)

# ukol 2 
def vypisPrvniprvek(pole):
    if len(pole) > 0:
        print(pole[0])
    else:
        print("Pole je prázdné.")
vypisPrvniprvek([10,20,30,15])

# ukol 3 
pocet = int(input("Zadejte hodnotu proměnné 'pocet': "))
cislo = int(input("Zadejte hodnotu proměnné 'cislo'"))

def sectiCisla(pocet,cislo):
    print(pocet+cislo)
sectiCisla(pocet, cislo)

# ukol 4 
jméno = input("Zadejte jméno postavy: ")
popis = input("popiš svojí postavu: ")
vek = int(input("Zadejte věk své postavy: "))
def fiktivniPostava(jméno,popis,vek):
    print(f"Nová postava se jmenuje {jméno}, je to {popis}, a je jí/mu {vek}")
fiktivniPostava(jméno, popis, vek)
