#ukol 4
zvirata = ["klokan", "koala", "kralik", "pes"]
print(zvirata[1])
print(zvirata[3])

#ukol 5 
seznam = []
seznam.append(10)
seznam.append(1)
seznam.append(12)
print(seznam)

#ukol 6
filmy = ["Rychle a zbesile", "Harry potter", "Mama Mia", "Herkules", "Hra o truny", "Pán prstenů", "Marvel"]
for filmy in filmy: 
    print(filmy)

#ukol 7 
cisla = [3,2,5]
cisla[1] = 999
print(cisla)

#ukol 8 
cislaLibovolna = [5,7,12,21,9]
soucet = sum(cislaLibovolna)
print(soucet)

#ukol 9 
random = [9,8,5,6,7,2,12,14,15]
len(random)
print(len(random))

#ukol 10 
znamky=[2,1,3,1,2,2]
prumer=sum(znamky)/len(znamky)
print(prumer)

#11
ovoce=["jahoda", "broskev", "jablko", "mango", "banán"]
for o in ovoce:
    if o=="banán":
        print("Banán je tam!!")
    else:
        print("Banán tam není...")

#12
seznamCisel=[71,5,32,4,9,12]
pocetVetsichCisel=0
for cislo in seznamCisel:
    if cislo>10:
        pocetVetsichCisel+=1
print("Počet čísel větších než 10 je: ", pocetVetsichCisel)

#13
Znamky = []
pocetZnamek = int(input("Zadejte kolik známek chcete zadat: "))
 
for i in range(pocetZnamek):
    Znamka = int(input(f"Zadej známku číslo {i + 1}: "))
    Znamky.append(Znamka)
