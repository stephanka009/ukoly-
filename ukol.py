skore = []
print("Zadejte skóre 10 hráčů (0 až 60):")
for i in range(10):
    bod = int(input(f"Hráč {i+1}: "))
    skore.append(bod)

print ("\nSkóre hráčů:", skore)

prumer = sum(skore) / 10 
nejvyssi = max(skore)
nejnizsi = min(skore)
print("průměrné skóre:", prumer)
print("Njevyšší skóre: ", nejvyssi)
print("nejnižší skóre: ", nejnizsi)

nad_50 = 0
for bod in skore:
    if bod > 50:
        nad_50 += 1
if nad_50 > 5:
    print("Výborný výkon!")
else:
    print("Můžete to příště zkusit lépe.")