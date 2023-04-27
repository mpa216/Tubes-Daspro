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
                    arrCandi[i][0] = str(i)
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


# Untuk testing
# userAktif = "dhika"
# arrBahan[0][2] = 100000
# arrBahan[1][2] = 100000
# arrBahan[2][2] = 100000
# arrCandi[1] = ['1', 'dhika', '2', '3', '4']
# arrCandi[3] = ['3', 'dhika', '4', '3', '2']
# gaming = True
# count = 104
# while True :
#     play = input("command?")   
#     if play == "bangun" :
#         for i in range(104) :          
#             bangun(userAktif)
#         print(arrCandi[99])
#         print(arrBahan)
#         print(lengthcandi(arrCandi))
#         count += 1

#     else :
#         gaming = False
