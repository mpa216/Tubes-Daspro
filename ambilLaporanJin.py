
                                                          # VERSI        ROMBAK #
arrUser     = [[str("inf") for cols in range (3)] for rows in range(102)] # array 2 dimensi (102 x 3) dengan index 0 dimiliki Bandung, 1 dimiilki Roro, dan 2-101 milik para jin
# arrUser[x][0], arrUser[x][1], arrUser[x][2] = Username, Password, Role
# Contoh [["Si Cakep","Saya cakep","Saya Cakep"], ..... , ["Bandung","Bondowoso","Antagonist"] ,["Roro","Jonggrang","Protagonist"]]
userAktif = "" # ini berisi username dari pengguna yg aktif, if useraktif == Bandung : ...... elif useraktif == Roro : ....... else #jin : ......
roleAktif = "" # ini berisi role dari pengguna yg aktif
jenisJin = [] # 0: pengumpul 1: pembangun, array ini isinya integer
usernameJinPembangun = [] # array 1 dimensi yang berisi nama-nama jin pembangun yang sudah ditandai dengan index
# Contoh ["Si Cakep", "Si Hebat", ....]
passwordJinPembangun = [] # array 1 dimensi yang berisi password-password jin pembangun yang sudah ditandai dengan index
# Contoh ["Saya cakep", "Saya hebat", ....]
usernameJinPengumpul = [] # array 1 dimensi yang berisi nama-nama jin pengumpul yang sudah ditandai dengan index
# Contoh ["Si Kuat", "Si Gigih", ....]
passwordJinPengumpul = [] # array 1 dimensi yang berisi password-password jin pengumpul yang sudah ditandai dengan index
# Contoh ["Saya kuat", "Saya gigih", ....]
arrCandi    = [[str("inf") for cols in range (5)] for rows in range(100)] # array 2 dimensi (100 x 5) dengan 
# arrCandi[x][0] = id candi, arrCandi[x][1] = Nama jin pembangunnya, arrCandi[x][2] = jumlah pasir/candi, arrCandi[x][3] = jumlah batu/candi, arrCandi[x][4] = jumlah air/candi
# Contoh [[1,"Si Cakep",5,3,4],[2,"Si Hebat",4,3,5], ....]
arrBahan = [['pasir', 'blank', 'inf'], ['batu', 'blank', 'inf'], ['air', 'blank', 'inf']]
#arrBahan    = [[str("inf") for cols in range (3)] for rows in range(3)] # array 2 dimensi (3 x 3) dengan index 0,1,2 menunjukkan jumlah pasir,batu, air secara berturut
                    # arrBahan[0][0], arrBahan[0][1], arrBahan[0][2] = "Pasir", "Blank", jumlah
# Maksud deskripsi  # arrBahan[1][0], arrBahan[1][1], arrBahan[1][2] = "Batu", "Blank", jumlah
                    # arrBahan[2][0], arrBahan[2][1],arrBahan[2][2] = "Air", "Blank", jumlah
# Contoh [["Pasir","Blank", 40], ["Batu","Blank","30"],["Air","Blank","50"]]


# arrUser[0][2] = "Pembangun"
# arrUser[1][2] = "Pembangun"  # ----> kalo mo test case
# arrUser[2][2] = "Pengumpul"

# arrCandi[0][0],arrCandi[0][1] = "1","Si Caka"
# arrCandi[1][0],arrCandi[1][1] = "2","Si Cakep"
# arrCandi[2][0],arrCandi[2][1] = "3","Si Cakep" # ----> kalo mo test case
# arrCandi[3][0],arrCandi[3][1] = "4","Si Assna"
# arrCandi[4][0],arrCandi[4][1] = "5","Si Assna"
# arrCandi[5][0],arrCandi[5][1] = "6","Si Test"

# arrBahan[0][2] = "5"
# arrBahan[1][2] = "6" # --> kalo mo test case
# arrBahan[2][2] = "7"

def hitungJin(arrUser):
    global totalJin
    totalJin = 0
    for i in range(102):
        if ((arrUser[i][2] == "Pembangun")  or (arrUser[i][2] == "Pengumpul")):
            totalJin += 1
    

def hitungJinPengumpul(arrUser):
    global totalJinPengumpul
    totalJinPengumpul = 0
    for i in range(102):
        if (arrUser[i][2] == 'Pengumpul'):
            totalJinPengumpul += 1


def hitungJinPembangun(arrUser):
    global totalJinPembangun
    totalJinPembangun = 0
    for i in range(102):
        if (arrUser[i][2] == "Pembangun"):
            totalJinPembangun += 1
    
    
hitungJin(arrUser)
hitungJinPengumpul(arrUser)
hitungJinPembangun(arrUser)

# ---------------------------------------------------------------   
excludeString = str("inf")

def siapaRajin(arrCandi, excludeString, paraRajin):
    count = [0] * 100
    max_count = count[0]
    for i in range(100):
        if excludeString and arrCandi[i][1] == excludeString:
            continue
        for j in range(i+1, 100):
            if excludeString and arrCandi[j][1] == excludeString:
                continue
            if arrCandi[i][1] == arrCandi[j][1]:
                count[i] += 1
                count[j] += 1
    for i in range(1,100):
        if count[i] > max_count:
            max_count = count[i]            
    for i in range(100):
        if count[i] == max_count and (excludeString is None or arrCandi[i][1] != excludeString):
            paraRajin[i] = arrCandi[i][1]


paraRajin = [str("inf")] * 100

siapaRajin(arrCandi, excludeString, paraRajin)

siRajin = paraRajin[0]
for i in range(1, 100):
    if paraRajin[i] != str("inf"):
        if paraRajin[i] < siRajin:
            siRajin = paraRajin[i]
        
if (siRajin == str("inf")):
    siRajin = "-"

# -----------------------------------------------------------------------------------------------------------------------------------
def siapaMalas(arrCandi, excludeString, paraMalas):
    count = [0] * 100
    for i in range(100):
        if excludeString and arrCandi[i][1] == excludeString:
            continue
        for j in range(i+1, 100):
            if excludeString and arrCandi[j][1] == excludeString:
                continue
            if arrCandi[i][1] == arrCandi[j][1]:
                count[i] += 1
                count[j] += 1
    min_count = 100
    for i in range(100):
        if count[i] < min_count and (excludeString is None or arrCandi[i][1] != excludeString):
            min_count = count[i]
    
    for i in range(100):
        if count[i] == min_count and (excludeString is None or arrCandi[i][1] != excludeString):
            paraMalas[i] = arrCandi[i][1]
    
paraMalas = [str("inf")] * 100

excludeString = str("inf")
siapaMalas(arrCandi, excludeString, paraMalas)

siMalas = paraMalas[0]
for i in range(1,100):
    if paraMalas[i] != str("inf"):
        if (siMalas == str("inf")):
            siMalas = paraMalas[i]
        if paraMalas[i] > siMalas:
            siMalas = paraMalas[i]   
            
if (siMalas == str("inf")):
    siMalas = "-"
# ----------------------------------------------------------------------------------

pasir = arrBahan[0][2]  
air = arrBahan[2][2]    
batu = arrBahan[1][2]    
 
if (pasir == "inf"):
    pasir = "0"
if (air == "inf"):
    air = "0"
if (batu == "inf"):
    batu = "0"

def laporanJin():
    print(f"Total Jin: {totalJin} ")
    print(f"Total Jin Pengumpul: {totalJinPengumpul}")
    print(f"Total Jin Pembangun: {totalJinPembangun} ")
    print(f"Jin Terajin: {siRajin}  ")
    print(f"Jin Termalas: {siMalas}")
    print(f"Jumlah Pasir:{pasir} ")
    print(f"Jumlah Air: {air}")
    print(f"Jumlah Batu: {batu} ")

# laporanJin() # --> kalo mo test case

