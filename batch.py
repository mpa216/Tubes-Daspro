import random
import FungsiUtama

arrCandi    = [[str("inf") for cols in range (5)] for rows in range(100)] # array 2 dimensi (100 x 5) dengan 
# arrCandi[x][0] = id candi, arrCandi[x][1] = Nama jin pembangunnya, arrCandi[x][2] = jumlah pasir/candi, arrCandi[x][3] = jumlah batu/candi, arrCandi[x][4] = jumlah air/candi
# Contoh [[1,"Si Cakep",5,3,4],[2,"Si Hebat",4,3,5], ....]
arrBahan = [['pasir', 'blank', 'inf'], ['batu', 'blank', 'inf'], ['air', 'blank', 'inf']]
# arrBahan    = [[str("inf") for cols in range (3)] for rows in range(3)] # array 2 dimensi (3 x 3) dengan index 0,1,2 menunjukkan jumlah pasir,batu, air secara berturut
                    # arrBahan[0][0], arrBahan[0][1], arrBahan[0][2] = "Pasir", "Blank", jumlah
# Maksud deskripsi  # arrBahan[1][0], arrBahan[1][1], arrBahan[1][2] = "Batu", "Blank", jumlah
                    # arrBahan[2][0], arrBahan[2][1],arrBahan[2][2] = "Air", "Blank", jumlah
# Contoh [["Pasir","Blank", 40], ["Batu","Blank","30"],["Air","Blank","50"]]
arrUser     = [[str("inf") for cols in range (3)] for rows in range(102)] # array 2 dimensi (102 x 3) dengan index 0-99 milik para jin, 100 dimiilki Bandung, 101 dimiliki Roro
# arrUser[x][0], arrUser[x][1], arrUser[x][2] = Username,Role, Password
# Contoh [["Si Cakep","Jin Pembangun","Saya cakep"], ..... , ["Bandung","Antagonist", "Bondowoso"] ,["Roro","Protagonist", "Jonggrang"]]
userAktif = "" # ini berisi username dari pengguna yg aktif, if useraktif == Bandung : ...... elif useraktif == Roro : ....... else #jin : ......

def batchkumpul():
    global arrUser
    global arrBahan

    lengthkumpul = 0
    jinkumpul = []
    for i in range(102) :
        if arrUser[i][2] == "jin_pengumpul" :
            jinkumpul = mappend(jinkumpul, arrUser[i][0])
            lengthkumpul += 1 
    if lengthkumpul == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else: 
        print(f"Mengerahkan {lengthkumpul} jin untuk mengumpulkan bahan.")  
        totalpasir = 0
        totalbatu = 0
        totalair = 0
        for i in range(lengthkumpul) :
            pasirkumpul = random.randint(0, 5)
            batukumpul = random.randint(0, 5)
            airkumpul = random.randint(0, 5)
            totalpasir += pasirkumpul
            totalbatu += batukumpul
            totalair += airkumpul
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
        print(f"Jin menemukan total {totalpasir} pasir, {totalbatu} batu, dan {totalair} air.")
        return    

def batchbangun():
    global arrCandi
    global arrBahan
    global arrUser

    jinbangun = []
    lengthbangun = 0
    bahantiapjin = []
    for i in range(102) :
        if arrUser[i][2] == "jin_pembangun" :
            jinbangun = mappend(jinbangun, arrUser[i][0])
            lengthbangun += 1

    if lengthbangun == 0 :
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        return
    else :
        # total ini adalah total yg dibutuhkan, bukan yg tersedia
        totalpasir = 0
        totalbatu = 0
        totalair = 0
        for i in range(lengthbangun) :
            pasir = random.randint(1, 5)
            batu = random.randint(1, 5)
            air = random.randint(1, 5)
            bahantiapjin = mappend(bahantiapjin, [pasir, batu, air])
            totalpasir += pasir
            totalbatu += batu
            totalair += air
        # pasir,batu, dan air real adalah jumlah bahan yg tersedia pada saat itu
        pasirreal = int(arrBahan[0][2])
        batureal = int(arrBahan[1][2])
        airreal = int(arrBahan[2][2])

        if pasirreal >= totalpasir and batureal >= totalbatu and airreal >= totalair :
            arrBahan[0][2] = str(pasirreal - totalpasir)
            arrBahan[1][2] = str(batureal - totalbatu)
            arrBahan[2][2] = str(airreal - totalair) 
            if lengthcandi(arrCandi) == 100 :
                print(f"Mengerahkan {lengthbangun} jin untuk membangun candi dengan total bahan {pasirreal} pasir, {batureal} batu, dan {airreal} air.")
                print(f"Jin berhasil membangun total {lengthbangun} candi.")
                return
            else :
                for j in range(lengthbangun) :
                    for i in range(100) :
                        if arrCandi[i][0] == "inf" :
                            arrCandi[i][0] = str(i)
                            arrCandi[i][1] = str(jinbangun[j])
                            arrCandi[i][2] = str(bahantiapjin[j][0])
                            arrCandi[i][3] = str(bahantiapjin[j][1])
                            arrCandi[i][4] = str(bahantiapjin[j][2])
                            break    
                print(f"Mengerahkan {lengthbangun} jin untuk membangun candi dengan total bahan {pasirreal} pasir, {batureal} batu, dan {airreal} air.")
                print(f"Jin berhasil membangun total {lengthbangun} candi.")    
                return
        else :
            print(f"Mengerahkan {lengthbangun} jin untuk membangun candi dengan total bahan {pasirreal} pasir, {batureal} batu, dan {airreal} air.")      
            kurangpasir = totalpasir - pasirreal
            kurangbatu = totalbatu - batureal
            kurangair = totalair - airreal
            if kurangpasir < 0 :
                kurangpasir = 0
            if kurangbatu < 0 :
                kurangbatu = 0
            if kurangair < 0 :
                kurangair = 0
            print(f"Bangun gagal. Kurang {kurangpasir} pasir, {kurangbatu} batu, dan {kurangair} air.")
            return
          
# Untuk testing
# arrUser[0] = ["Si Cakep","Saya cakep", "jin_pengumpul"]
# arrUser[1] = ["Si Jelek","Saya jelek", "jin_pengumpul"]
# arrUser[2] = ["Si Jelek","Saya jelek", "jin_pengumpul"]
# arrUser[3] = ["Si Jelek","Saya jelek", "jin_pengumpul"]
# arrUser[4] = ["Si anjing","Saya anjing", "jin_pembangun"]
# arrUser[5] = ["Si babi","Saya babi", "jin_pembangun"]


# for i in range(104) :
#     batchbangun()
# print(arrCandi)
# print(arrBahan)
# batchbangun()
# print(arrCandi)


# gaming = True
# while gaming :
#     play = input("command?")
#     if play == "batchkumpul" :
#         batchkumpul()
#         print(arrBahan)
#     elif play == "kumpul" :
#         kumpul()
#         print(arrBahan)
#     elif play == "batchbangun" :
#         batchbangun()
#         print(arrCandi)
#         print(arrBahan)
#     elif play == "bangun" :
#         bangun()
#         print(arrCandi)
#         print(arrBahan)
#     else :
#         gaming = False
