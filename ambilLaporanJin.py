import FungsiUtama
import standardvariables

def hitungJin(arrUser):
    global totalJin
    totalJin = 0
    arrUser = standardvariables.arrUser
    for i in range(102):
        if ((arrUser[i][2] == "Jin Pembangun")  or (arrUser[i][2] == "Jin Pengumpul")):
            totalJin += 1
    return totalJin

def hitungJinPengumpul(arrUser):
    global totalJinPengumpul
    totalJinPengumpul = 0
    arrUser = standardvariables.arrUser
    for i in range(102):
        if (arrUser[i][2] == 'Jin Pengumpul'):
            totalJinPengumpul += 1
    return totalJinPengumpul

def hitungJinPembangun(arrUser):
    global totalJinPembangun
    totalJinPembangun = 0
    arrUser = standardvariables.arrUser
    for i in range(102):
        if (arrUser[i][2] == "Jin Pembangun"):
            totalJinPembangun += 1
    return totalJinPembangun

pasir = standardvariables.arrBahan[0][2]  
air = standardvariables.arrBahan[2][2]    
batu = standardvariables.arrBahan[1][2]    
 
if (pasir == "inf"):
    pasir = "0"
if (air == "inf"):
    air = "0"
if (batu == "inf"):
    batu = "0"
    
hitungJin(standardvariables.arrUser)
hitungJinPengumpul(standardvariables.usernameJinPengumpul)
hitungJinPembangun(standardvariables.arrUser)

def laporanJin():
    print(f"Total Jin: {totalJin} ")
    print(f"Total Jin Pengumpul: {totalJinPengumpul}")
    print(f"Total Jin Pembangun: {totalJinPembangun} ")
    print(f"Jin Terajin:  ")
    print(f"Jin Termalas: ")
    print(f"Jumlah Pasir:{pasir} ")
    print(f"Jumlah Air: {air}")
    print(f"Jumlah Batu: {batu} ")

laporanJin()





    

  
    


