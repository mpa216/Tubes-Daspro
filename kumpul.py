import random
import FungsiUtama

def kumpul():
    pasirkumpul = random.randint(0, 5)
    batukumpul = random.randint(0, 5)
    airkumpul = random.randint(0, 5)
    bahansebelumkumpul = extract(2, "bahan_bangunan.csv")
    pasirsebelum = int(bahansebelumkumpul[0])
    batusebelum = int(bahansebelumkumpul[1])
    airsebelum = int(bahansebelumkumpul[2])
    pasirafter = pasirsebelum + pasirkumpul
    batuafter = batusebelum + batukumpul
    airafter = airsebelum + airkumpul
    update_bahan(pasirafter, batuafter, airafter)
    print(f"Jin Menemukan {pasirkumpul} pasir, {batukumpul} batu, dan {airkumpul} air.")
