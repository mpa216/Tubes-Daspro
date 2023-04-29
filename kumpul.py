def kumpul():
    global arrBahan

    pasirkumpul = random.randint(0, 5)
    batukumpul = random.randint(0, 5)
    airkumpul = random.randint(0, 5)
    if arrBahan[0][2] == "inf":
        arrBahan[0][2] = 0
    if arrBahan[1][2] == "inf":
        arrBahan[1][2] = 0
    if arrBahan[2][2] == "inf":
        arrBahan[2][2] = 0
    
    pasirsebelum = int(arrBahan[0][2])
    batusebelum = int(arrBahan[1][2])
    airsebelum = int(arrBahan[2][2])

    pasirafter = pasirsebelum + pasirkumpul
    batuafter = batusebelum + batukumpul
    airafter = airsebelum + airkumpul

    arrBahan[0][2] = str(pasirafter)
    arrBahan[1][2] = str(batuafter)
    arrBahan[2][2] = str(airafter)

    print(f"Jin Menemukan {pasirkumpul} pasir, {batukumpul} batu, dan {airkumpul} air.")
    return
