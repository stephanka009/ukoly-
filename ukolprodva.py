<<<<<<< HEAD
#Štefková, Riegerova
#b
aktivita1 = input("zadejte aktivitu jedna: ")
cas1 = int(input(f"Zadejte delku aktivity{aktivita1} v minutach: "))

aktivita2 = input("Zadejte druhou sportovni aktivitu: ")
cas2 = int(input(f"Zadejte delku aktivity {aktivita2} v minutach: "))

celkovyVydej = (cas1 + cas2) * 5 
print(f"Celkem spálené kalorie: {celkovyVydej} kcal")

#a
jidlo1=input("Zadejte jídlo: ")
kalorie1=int(input("Zadejte počet kalorií: "))
jidlo2=input("Zadejte jídlo: ")
kalorie2=int(input("Zadejte počet kalorií: "))
jidlo3=input("Zadejte jídlo: ")
kalorie3=int(input("Zadejte počet kalorií: "))
celkoveKalorie=kalorie1+kalorie2+kalorie3
print(celkoveKalorie) 

#dohromady ukol
celkovyVydej = (cas1 + cas2) * 5 
rozdil = celkoveKalorie - celkovyVydej

if rozdil > 0:
    print(f"přebytek: {rozdil:.f1} kcal")
elif rozdil < 0:
    print(f"Nedostatek: {-rozdil:.1f} kcal")
else:
=======
#Štefková, Riegerova
#b
aktivita1 = input("zadejte aktivitu jedna: ")
cas1 = int(input(f"Zadejte delku aktivity{aktivita1} v minutach: "))

aktivita2 = input("Zadejte druhou sportovni aktivitu: ")
cas2 = int(input(f"Zadejte delku aktivity {aktivita2} v minutach: "))

celkovyVydej = (cas1 + cas2) * 5 
print(f"Celkem spálené kalorie: {celkovyVydej} kcal")

#a
jidlo1=input("Zadejte jídlo: ")
kalorie1=int(input("Zadejte počet kalorií: "))
jidlo2=input("Zadejte jídlo: ")
kalorie2=int(input("Zadejte počet kalorií: "))
jidlo3=input("Zadejte jídlo: ")
kalorie3=int(input("Zadejte počet kalorií: "))
celkoveKalorie=kalorie1+kalorie2+kalorie3
print(celkoveKalorie) 

#dohromady ukol
celkovyVydej = (cas1 + cas2) * 5 
rozdil = celkoveKalorie - celkovyVydej

if rozdil > 0:
    print(f"přebytek: {rozdil:.f1} kcal")
elif rozdil < 0:
    print(f"Nedostatek: {-rozdil:.1f} kcal")
else:
>>>>>>> db7e84bd23d61ace5d43f3a3dbd865a120023721
    print("Kalorická bilance je vyrovnaná")