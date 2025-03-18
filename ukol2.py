cislo1 = float(input("Zadejte prvni desetinne cislo: "))
cislo2 = float(input("zadejte druhe desetinne cislo: "))

soucet = cislo1 + cislo2
rozdil = cislo1 - cislo2
soucin = cislo1 * cislo2
podil = cislo1 / cislo2 
if cislo2==0:
    print("Nelze dělit nulou")

print(f"soucet: {soucet:.2f}")
print(f"rozdil: {rozdil:.2f}")
print(f"soucin: {soucin:.2f}")
print(f"podil: {podil:.2f}"if isinstance(podil, float) else podil)