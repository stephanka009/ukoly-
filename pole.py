cisla = [12,15,7,22,20,21,41,42,46]

hledane = int(input("Zadejte číslo, které chcete v poli najít.: "))

if hledane in cisla :
    pozice = cisla.index(hledane)
    print(f"Našel jsem tuto hodnotu na pozici X")
else:
    print("Zadana hodnota tady není. ")