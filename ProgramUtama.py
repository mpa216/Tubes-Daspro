from FungsiUtama import tulis_header,length,lengthcandi,mappend,my_split,del_element,my_max,my_min,my_sort,append_lain,mappend_lain_2,hapus_space,len_lain,baca_csv
import random
import sys
import argparse
import os


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

arrUser[0] = ["Bondowoso","cintaroro","bandung_bondowoso"]
arrUser[1] = ["Roro","gasukabondo","roro_jonggrang"]
# arrUser[2] = ["jin1","gasukabondo","jin_pembangun"]
# arrUser[3] = ["jin2","gasukabondo","jin_pengumpul"]
# arrCandi[1][0] = "1"
# arrCandi[1][1] = "Si Cakep"
# arrCandi[1][2] = "2"
# arrCandi[1][3] = "3"
# arrCandi[1][4] = "4"
#                              #  ----> kaloo mo test case
# arrCandi[2][0] = "2"
# arrCandi[2][1] = "Si Hebat"
# arrCandi[2][2] = "4"
# arrCandi[2][3] = "2"
# arrCandi[2][4] = "5"

arrBahan[0][2] = "4"
arrBahan[1][2] = "5"
arrBahan[2][2] = "7"

def login():
        global arrUser
        global userAktif
        global roleAktif

        while userAktif=="":
            username_login, password_login = str(input("Username: ")), str(input("Password: "))
            for i in range (0,102):
                if arrUser[i][0]==username_login:
                    if arrUser[i][1]==password_login:
                        print(f'Selamat datang, {username_login}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.')
                        userAktif = str(username_login)
                        roleAktif = str(arrUser[i][2])
                        return
                        
                    else:
                        kondisi = ("Password salah!")
                        break
                else:
                    kondisi =("Username tidak terdaftar!")
            print(kondisi)
        if userAktif!="":
            print(f"Anda telah login dengan username {userAktif}, silahkan lakukan “logout” sebelum melakukan login kembali.  ")
            return

def logout():
    global userAktif
    global roleAktif
    if userAktif == "" :
        return
    else :
        userAktif = ""
        roleAktif = ""

def tambahJin():
    global arrUser
    x = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
    tambah = False
    while not (x==1 or x==2):
        print(f'Tidak ada jenis jin bernomor "{x}"')
        x = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
    if length(arrUser)<102:
        if x==1:
            tipe = "Pengumpul"
        else:
            tipe = "Pembangun"
        print(f"Memilih jin {tipe}.")
        username_jin = str(input("Masukkan username jin: "))
        password_jin = str(input("Masukkan password jin: "))
        for i in range (2,102):
            if arrUser[i][0]==username_jin:
                print(f'Username "{username_jin}" sudah diambil!')
                username_jin = str(input("Masukkan username jin: "))
                tambah = False
                break
            else:
                tambah = True
        if tambah:
            arrUser = append_lain(arrUser,[username_jin,password_jin,tipe])
        
    else:
        print("Jin sudah Penuh")
    return

def ubahtipe():
    global arrUser
    ada = False
    jinygdiubah = str(input("Masukkan username jin :"))
    for i in range (2,102):
        if arrUser[i][0]==jinygdiubah:
            ada = True
            break
    if ada:
        if arrUser[i][2]=="Pembangun":
            tipe = "Pengumpul"
        else:
            tipe = "Pembangun"
        masukan = str(input(f'Jin ini bertipe {arrUser[i][2]}. Yakin ingin mengubah ke tipe {tipe} (Y/N)? '))
        if masukan=='Y' or masukan=='y':
            arrUser[i][2]=tipe
            print("Jin telah berhasil diubah.")
        elif masukan=="N" or masukan=="n":
            print("Jin tidak jadi diubah.")
    else:
        print("Tidak ada jin dengan username tersebut.")
    return

def bangun():
    global arrBahan
    global arrCandi 

    pasir = random.randint(1, 5)
    batu = random.randint(1, 5)
    air = random.randint(1, 5)

    if arrBahan[0][2] == "inf" : 
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
        return
    else :
        pasirreal = int(arrBahan[0][2])
        batureal = int(arrBahan[1][2])
        airreal = int(arrBahan[2][2])
    
    if pasirreal >= pasir and batureal >= batu and airreal >= air :
        arrBahan[0][2] = str(pasirreal - pasir)
        arrBahan[1][2] = str(batureal - batu)
        arrBahan[2][2] = str(airreal - air) 
        if lengthcandi(arrCandi) == 100 :
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {100-lengthcandi(arrCandi)}.")
            return
        else :
            for i in range(100) :
                if arrCandi[i][0] == "inf" :
                    arrCandi[i][0] = str(i + 1)
                    arrCandi[i][1] = str(userAktif)
                    arrCandi[i][2] = str(pasir)
                    arrCandi[i][3] = str(batu)
                    arrCandi[i][4] = str(air)
                    print("Candi berhasil dibangun.")
                    print(f"Sisa candi yang perlu dibangun: {100-lengthcandi(arrCandi)}.")
                    return
    else :
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
        return
    
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
                arrBahan[0][2] = str(0)
            if arrBahan[1][2] == "inf":
                arrBahan[1][2] = str(0)
            if arrBahan[2][2] == "inf":
                arrBahan[2][2] = str(0)        
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
        if arrBahan[0][2] == "inf":
                arrBahan[0][2] = str(0)
        if arrBahan[1][2] == "inf":
                arrBahan[1][2] = str(0)
        if arrBahan[2][2] == "inf":
                arrBahan[2][2] = str(0)  
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
                            arrCandi[i][0] = str(i + 1)
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
        
def laporanjin():
    def hitungJin(arrUser):
        global totalJin
        totalJin = 0
        for i in range(102):
            if ((arrUser[i][2] == "jin_pembangun")  or (arrUser[i][2] == "jin_pengumpul")):
                totalJin += 1
        

    def hitungJinPengumpul(arrUser):
        global totalJinPengumpul
        totalJinPengumpul = 0
        for i in range(102):
            if (arrUser[i][2] == 'jin_pengumpul'):
                totalJinPengumpul += 1


    def hitungJinPembangun(arrUser):
        global totalJinPembangun
        totalJinPembangun = 0
        for i in range(102):
            if (arrUser[i][2] == "jin_pembangun"):
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

    def laporJin():
        print(f"Total Jin: {totalJin} ")
        print(f"Total Jin Pengumpul: {totalJinPengumpul}")
        print(f"Total Jin Pembangun: {totalJinPembangun} ")
        print(f"Jin Terajin: {siRajin}  ")
        print(f"Jin Termalas: {siMalas}")
        print(f"Jumlah Pasir:{pasir} ")
        print(f"Jumlah Air: {air}")
        print(f"Jumlah Batu: {batu} ")
    laporJin()

def laporancandi():
    totalCandi = lengthcandi(arrCandi)
    def hitungPasir():
        global usedPasir 
        usedPasir = 0
        for i in range(100):
            if arrCandi[i][2] != str("inf"):
                usedPasir += int(arrCandi[i][2])
            

    def hitungBatu():
        global usedBatu 
        usedBatu = 0
        for i in range(100):
            if arrCandi[i][3] != str("inf"):
                usedBatu += int(arrCandi[i][3])
    
    def hitungAir():
        global usedAir 
        usedAir = 0
        for i in range(100):
            if arrCandi[i][4] != str("inf"):
                usedAir += int(arrCandi[i][4])

    hitungPasir()
    hitungBatu()
    hitungAir()

    def hargaCandi():
        global candiAda
        global tajMahal
        global biayaTajMahal
        global tajMurah
        global biayaTajMurah
        global arrCandiHitung
        arrCandiHitung = [[str("0") for cols in range(5)] for rows in range(100)]
        for i in range(100):
            if (arrCandiHitung[i] != arrCandi[i]):
                arrCandiHitung[i] = arrCandi[i]
        for i in range(100):
            if (arrCandiHitung[i][0] == str("inf")):
                arrCandiHitung[i] = ["0","0","0","0","0"]
        candiAda = [[0 for cols in range(2)] for rows in range(101)]
        for i in range(100):
            if (arrCandiHitung[i][0] != str("inf")):
                candiAda[i][0] = arrCandiHitung[i][0]
                candiAda[i][1] = (int(arrCandiHitung[i][2])*10000) + (int(arrCandiHitung[i][3])*15000) + (int(arrCandiHitung[i][4])*7500)

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


    def laporCandi():
        if totalCandi == 0:
            print(f"Total Candi: {totalCandi}")
            print(f"Total Pasir yang digunakan: {usedPasir}")
            print(f"Total Batu yang digunakan: {usedBatu}")
            print(f"Total Air yang digunakan: {usedAir}")
            print(f"ID Candi Termahal: -")
            print(f"ID Candi Termurah: -")
        else:
            print(f"Total Candi: {totalCandi}")
            print(f"Total Pasir yang digunakan: {usedPasir}")
            print(f"Total Batu yang digunakan: {usedBatu}")
            print(f"Total Air yang digunakan: {usedAir}")
            print(f"ID Candi Termahal: {tajMahal} (Rp {biayaTajMahal})")
            print(f"ID Candi Termurah: {tajMurah} (Rp {biayaTajMurah})")
            

    laporCandi()
    return

def hancurkancandi():
    global arrCandi
    id = input("Masukkan ID candi: ")
    for i in range(100):
        if (arrCandi[i][0] == id):
            print(f"Apakah anda ingin menghancurkan candi ID: {id} (Y/N)?")
            jawab = input()
            if (jawab == "Y") or (jawab == "y"):
                arrCandi[i][0] = str('inf')
                arrCandi[i][1] = str('inf')
                arrCandi[i][2] = str('inf')
                arrCandi[i][3] = str('inf')
                arrCandi[i][4] = str('inf')
                print("Candi telah berhasil dihancurkan.")
                break
            elif (jawab == "N") or (jawab == "n"):
                print("Candi tidak jadi dihancurkan.")
                break
        else:
            if (i == 100-1):
                print("Tidak ada candi dengan ID tersebut.")
                break
    return

def ayam_berkokok():
    # global arrCandi
    jumlahCandi = lengthcandi(arrCandi)

    if (jumlahCandi) < (100):
        print("Kukuruyuk.. Kukuruyuk.. \n")
        print(f"Jumlah Candi: {jumlahCandi} \n ")
        print("Selamat, Roro Jonggrang memenangkan permainan! \n")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
        exit()
    else:
        print("Kukuruyuk.. Kukuruyuk.. \n")
        print(f"Jumlah Candi: {jumlahCandi} \n ")
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        exit()

def exit():
    salah = True
    while salah :
        simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if simpan == "y" : 
            #save()
            sys.exit()
        elif simpan == "n" :
            sys.exit()

def help():
    notLogin = """
    1. login - untuk menggunakan akun
    2. exit - untuk keluar dari program dan kembali ke terminal
    """
    bandung = """
    1. logout - untuk keluar dari akun yang digunakan sekarang
    2. summonjin - untuk memanggila jin
    3. hapusjin - untuk menghapus jin
    4. ubahjin - untuk mengubah tipe jin
    5. batchkumpul/bangun - untuk mengerahkan seluruh pasukan jin untuk mengumpulkan bahan atau pembangun
    6. laporanjin - untuk mengambil laporan jin atas kinerja para jin
    7. laporancandi - untuk mengambil laporan candi untuk mengetahui progress pembangunan candi
    8. exit - untuk keluar dari program dan kembali ke terminal
    """
    roro = """
    1. logout - untuk keluar dari akun yang digunakan sekarang
    2. hancurkancandi - untuk menghancurkan candi yang tersedia
    3. ayamberkokok - untuk menyelesaikan permainan dengan memalsukan pagi hari
    4. exit - untuk keluar dari program dan kembali ke terminal
    """
    jinPengumpul = """
    1. logout - untuk keluar dari akun yang digunakan sekarang
    2. kumpul - untuk mengumpulkan candi
    3. exit - untuk keluar dari program dan kembali ke terminal
    """
    jinPembangun = """
    1. logout - untuk keluar dari akun yang digunakan sekarang
    2. bangun - untuk membangun candi
    3. exit - untuk keluar dari program dan kembali ke terminal
    """  
    if roleAktif == "":
        print("===========HELP===========")
        print(notLogin)
    else:
        if roleAktif == "bandung_bondowoso":
            print("===========HELP===========")
            print(bandung)
        elif roleAktif == "roro_jonggrang":
            print("===========HELP===========")
            print(roro)
        elif roleAktif == "jin_pengumpul":
            print("===========HELP===========")
            print(jinPengumpul)
        elif roleAktif == "jin_pembangun":
            print("===========HELP===========")
            print(jinPembangun)
    return

def hilangkanjin():
    global arrUser
    global arrCandi

    jin_hilang = str(input("Masukkan username jin : "))
    kondisi= False
    for i in range (2,102):
        if arrUser[i][0]==jin_hilang:
            kondisi = True
            break
    if kondisi:
        hilang = str(input(f"Apakah anda yakin ingin menghapus jin dengan username {jin_hilang} (Y/N)? "))
        while not (hilang=="y" or hilang=="Y" or hilang=="N" or hilang=="n"):
            print("Input salah.")
            hilang = str(input(f"Apakah anda yakin ingin menghapus jin dengan username {jin_hilang} (Y/N)? "))
        if hilang=='Y' or hilang=='y':
            for j in range (2,101):
                arrUser[j]=arrUser[j+1]
            arrUser[101] = ['inf','inf','inf']
            for j in range (100):
                if arrCandi[j][1]==jin_hilang:
                    arrCandi[j]=['inf','inf','inf','inf','inf']
        elif hilang=="N" or hilang=="n":
            print("Jin tidak jadi dihilangkan.")
    else :
        print("Tidak ada jin dengan username itu")

    return




on = True
while on :
    while roleAktif == "" :
        # print(arrUser)
        cmd = input("cmd: ")
        if cmd == "login" :
            login()
        elif cmd == "help" :
            help()
        elif cmd == "exit" :
            exit()
        else :
            print("Anda belum login, silahkan login terlebih dahulu")
    while roleAktif == "bandung_bondowoso" :
        # print(arrCandi)
        # print(arrUser)
        # print(arrBahan)
        cmd = input("cmd: ")
        if cmd == "logout" :
            logout()
        elif cmd == "summonjin" :
            print(length(arrUser))
            tambahJin()
        elif cmd == "hapusjin" :
            hilangkanjin()
        elif cmd == "ubahjin" :
            ubahtipe()
        elif cmd == "batchkumpul" :
            batchkumpul()
        elif cmd == "batchbangun" :
            batchbangun()
        elif cmd == "laporanjin" :
            laporanjin()
        elif cmd == "laporancandi" :
            laporancandi()
        elif cmd == "exit" :
            exit()
        elif cmd == "help" :
            help()
        elif cmd == "login" :
            login()
        else :
            print("Anda tidak memiliki akses ke fitur tersebut")

    while roleAktif == "roro_jonggrang" :
        # print(arrCandi)
        cmd = input("cmd: ")
        if cmd == "logout" :
            logout()
        elif cmd == "hancurkancandi" :
            hancurkancandi()
        elif cmd == "ayamberkokok" :
            ayam_berkokok()
        elif cmd == "exit" :
            exit()
        elif cmd == "help" :
            help()
        elif cmd == "login" :
            login()
        else :
            print("Anda tidak memiliki akses ke fitur tersebut")
    while roleAktif == "jin_pengumpul" :
        # print(arrBahan)
        cmd = input("cmd: ")
        if cmd == "logout" :
            logout()
        elif cmd == "kumpul" :
            kumpul()
        elif cmd == "exit" :
            exit()
        elif cmd == "login" :
            login()
        else :
            print("Anda tidak memiliki akses ke fitur tersebut")
    while roleAktif == "jin_pembangun" :
        # print(arrCandi)
        # print(arrBahan)
        cmd = input("cmd: ")
        if cmd == "logout" :
            logout()
        elif cmd == "bangun" :
            bangun()
        elif cmd == "exit" :
            exit()
        elif cmd == "login" :
            login()
        else :
            print("Anda tidak memiliki akses ke fitur tersebut")

def load(nama_folder):
    global arrUser
    global arrCandi
    global arrBahan
    #Cek apakah folder ada
    if not os.path.exists(nama_folder):
        print(f"Folder '{nama_folder}' tidak ditemukan.")
        return

    #Load data dari file-file dalam folder
    else:
        with open(f'{nama_folder}\\user.csv', 'r') as file:
            data_user = baca_csv(file.name, delimiter=";")
            for i in range (1,len_lain(data_user)):
                for j in range (3):
                    arrUser[i-1][j]=data_user[i][j]
                if arrUser[i-1][2]!='inf':
                    arrUser[i-1][2] = hapus_space(arrUser[i-1][2])
            print(arrUser)
            
        with open(f'{nama_folder}\\candi.csv', 'r') as file:
            data_candi = baca_csv(file.name, delimiter=";")
            for i in range (1,len_lain(data_candi)):
                for j in range (5):
                    arrCandi[int(data_candi[i][0])-1][j]=data_candi[i][j]
                if arrCandi[int(data_candi[i][0])-1][4]!='inf':
                    arrCandi[int(data_candi[i][0])-1][4] = hapus_space(arrCandi[int(data_candi[i][0])-1][4])
            print(arrCandi)

        with open(f'{nama_folder}\\bahan_bangunan.csv', 'r') as file:
            data_bahan = baca_csv(file.name, delimiter=";")
            for i in range (1,len_lain(data_bahan)):
                for j in range (3):
                    arrBahan[i-1][j]=data_bahan[i][j]
                if arrBahan[i-1][2]!='inf':
                    arrBahan[i-1][2] = hapus_space(arrBahan[i-1][2])
            print(arrBahan)
            return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Prosedur untuk memuat data dari file-file dalam suatu folder.")
    parser.add_argument('nama_folder', type=str, help="Nama folder yang berisi file-file penyimpanan.")
    args = parser.parse_args()
    load(args.nama_folder)

def save():
    global arrUser
    global arrCandi
    global arrBahan
    #Cek apakah folder ada
    nama_folder = str(input(""))
    path = f'save\\{nama_folder}'

    print("Saving...")
    if not os.path.exists(path):
        print(f"Membuat folder save/{nama_folder}...")
        os.mkdir(path)
    print(f"Berhasil menyimpan data di folder {nama_folder}")
    with open(f"{path}\\user.csv", "a") as file:
        skip = True
        tulis_header("username;password;role",f"{path}\\user.csv")
        for row in range (102):
            for col in range (3):
                if arrUser[row][col]!='inf':
                    if col<2:
                        file.write(str(arrUser[row][col]) + ";")
                    else:
                        file.write(str(arrUser[row][col]))
                    skip = False
            if not skip:
                file.write("\n")
            skip=True
        
    with open(f"{path}\\candi.csv", "a") as file:
        skip = True
        tulis_header("id;pembuat;pasir;batu;air",f"{path}\\candi.csv")
        for row in range (100):
            for col in range (5):
                if arrCandi[row][col]!='inf':
                    if col<4:
                        file.write(str(arrCandi[row][col]) + ";")
                    else:
                        file.write(str(arrCandi[row][col]))
                    skip = False
            if not skip:
                file.write("\n")
            skip=True

    with open(f"{path}\\bahan_bangunan.csv", "a") as file:
        skip = True
        tulis_header("nama;deskripsi;jumlah",f"{path}\\bahan_bangunan.csv")
        for row in range (3):
            for col in range (3):
                if arrBahan[row][col]!='inf':
                    if col<2:
                        file.write(str(arrBahan[row][col]) + ";")
                    else:
                        file.write(str(arrBahan[row][col]))
                    skip = False
            if not skip:
                file.write("\n")
            skip=True
    return
