import random
import FungsiUtama

arrCandi    = [[str("inf") for cols in range (5)] for rows in range(100)] # array 2 dimensi (100 x 5) dengan 
# arrCandi[x][0] = id candi, arrCandi[x][1] = Nama jin pembangunnya, arrCandi[x][2] = jumlah pasir/candi, arrCandi[x][3] = jumlah batu/candi, arrCandi[x][4] = jumlah air/candi
# Contoh [[1,"Si Cakep",5,3,4],[2,"Si Hebat",4,3,5], ....]
arrBahan    = [[str("inf") for cols in range (3)] for rows in range(3)] # array 2 dimensi (3 x 3) dengan index 0,1,2 menunjukkan jumlah pasir,batu, air secara berturut
                    # arrBahan[0][0], arrBahan[0][1], arrBahan[0][2] = "Pasir", "Blank", jumlah
# Maksud deskripsi  # arrBahan[1][0], arrBahan[1][1], arrBahan[1][2] = "Batu", "Blank", jumlah
                    # arrBahan[2][0], arrBahan[2][1],arrBahan[2][2] = "Air", "Blank", jumlah
# Contoh [["Pasir","Blank", 40], ["Batu","Blank","30"],["Air","Blank","50"]]
arrBahan = [['pasir', 'blank', 'inf'], ['batu', 'blank', 'inf'], ['air', 'blank', 'inf']]
# arrUser     = [[str("inf") for cols in range (3)] for rows in range(102)] # array 2 dimensi (102 x 3) dengan index 0-99 milik para jin, 100 dimiilki Bandung, 101 dimiliki Roro
# arrUser[x][0], arrUser[x][1], arrUser[x][2] = Username,Role, Password
# Contoh [["Si Cakep","Jin Pembangun","Saya cakep"], ..... , ["Bandung","Antagonist", "Bondowoso"] ,["Roro","Protagonist", "Jonggrang"]]
userAktif = "" # ini berisi username dari pengguna yg aktif, if useraktif == Bandung : ...... elif useraktif == Roro : ....... else #jin : ......

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

# Untuk testing
# gaming = True
# while gaming :
#     play = input("command?")
#     if play == "kumpul":
#         kumpul()
#         print(arrBahan)
#     else :
#         gaming = False
#
