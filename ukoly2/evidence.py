def pridejZvire(seznam, jmeno, druh):
    seznam.append((jmeno, druh))

def vypisZvirata(seznam):
    if not seznam:
        print("Seznam zvířat je prázdný.")
    else:
        for i, (jmeno, druh) in enumerate(seznam, start=1):
            print(f"{i}. {jmeno} ({druh})")
