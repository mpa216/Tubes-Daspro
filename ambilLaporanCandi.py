from FungsiUtama import lengthcandi

arrUser     = [[str("inf") for cols in range (3)] for rows in range(102)] # array 2 dimensi (102 x 3) dengan index 0 dimiliki Bandung, 1 dimiilki Roro, dan 2-101 milik para jin
# arrUser[x][0], arrUser[x][1], arrUser[x][2] = Username, Password, Role
# Contoh [["Si Cakep","Jin Pembangun","Saya cakep"], ..... , ["Bandung","Antagonist", "Bondowoso"] ,["Roro","Protagonist", "Jonggrang"]]
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



# arrCandi[0][0] = 1
# arrCandi[0][1] = "Si Cakep"
# arrCandi[0][2] = 2
# arrCandi[0][3] = 3
# arrCandi[0][4] = 4
                               # ----> kaloo mo test case
# arrCandi[1][0] = 2
# arrCandi[1][1] = "Si Hebat"
# arrCandi[1][2] = 4
# arrCandi[1][3] = 2
# arrCandi[1][4] = 5


totalCandi = lengthcandi(arrCandi)

def hitungPasir():
    global usedPasir
    global arrCandi 
    usedPasir = 0
    for i in range(100):
        if arrCandi[i][2] != str("inf"):
            usedPasir += int(arrCandi[i][2])
        

def hitungBatu():
    global usedBatu 
    global arrCandi
    usedBatu = 0
    for i in range(100):
        if arrCandi[i][3] != str("inf"):
            usedBatu += int(arrCandi[i][3])
   
def hitungAir():
    global usedAir 
    global arrCandi
    usedAir = 0
    for i in range(100):
        if arrCandi[i][4] != str("inf"):
            usedAir += int(arrCandi[i][4])

hitungPasir()
hitungBatu()
hitungAir()

def hargaCandi():
    global arrCandi
    global candiAda
    global tajMahal
    global biayaTajMahal
    global tajMurah
    global biayaTajMurah
    candiAda = [[0 for cols in range(2)] for rows in range(101)]
    for i in range(totalCandi):
        if (arrCandi[i][0] != str("inf")):
            candiAda[i][0] = arrCandi[i][0]
            candiAda[i][1] = (int(arrCandi[i][2])*10000) + (int(arrCandi[i][3])*15000) + (int(arrCandi[i][4])*7500)
    tajMahal = candiAda[0][0]
    biayaTajMahal = float("-inf")      
    for i in range(100):
        if candiAda[i][1] > biayaTajMahal:
            tajMahal = candiAda[i][0]
            biayaTajMahal = candiAda[i][1]
    tajMurah = candiAda[0][0]
    biayaTajMurah = float("inf")
    for i in range(100):
        if (candiAda[i][1] != 0):
            if candiAda[i][1] < biayaTajMurah:
                tajMurah = candiAda[i][0]
                biayaTajMurah = candiAda[i][1]           

            
hargaCandi()


def laporanCandi():
    if ((tajMahal != 0) and (tajMurah != 0)):
        print(f"Total Candi: {totalCandi}")
        print(f"Total Pasir yang digunakan: {usedPasir}")
        print(f"Total Batu yang digunakan: {usedBatu}")
        print(f"Total Air yang digunakan: {usedAir}")
        print(f"ID Candi Termahal: {tajMahal} (Rp {biayaTajMahal})")
        print(f"ID Candi Termurah: {tajMurah} (Rp {biayaTajMurah})")
    elif ((tajMahal == 0) and (tajMurah == 0)):
        print(f"Total Candi: {totalCandi}")
        print(f"Total Pasir yang digunakan: {usedPasir}")
        print(f"Total Batu yang digunakan: {usedBatu}")
        print(f"Total Air yang digunakan: {usedAir}")
        print(f"ID Candi Termahal: -")
        print(f"ID Candi Termurah: -")

# laporanCandi() --> kalo mo test case
