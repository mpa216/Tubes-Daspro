import FungsiUtama
import standardvariables

totalCandi = FungsiUtama.lengthcandi(standardvariables.arrCandi)

def hitungPasir(arrCandi):
    global usedPasir 
    usedPasir = 0
    arrCandi = standardvariables.arrCandi
    for i in range(100):
        if arrCandi[i][2] != str("inf"):
            usedPasir += int(arrCandi[i][2])
        

def hitungBatu(arrCandi):
    global usedBatu 
    usedBatu = 0
    arrCandi = standardvariables.arrCandi
    for i in range(100):
        if arrCandi[i][3] != str("inf"):
            usedBatu += int(arrCandi[i][3])
   
def hitungAir(arrCandi):
    global usedAir 
    usedAir = 0
    arrCandi = standardvariables.arrCandi
    for i in range(100):
        if arrCandi[i][4] != str("inf"):
            usedAir += int(arrCandi[i][4])

hitungPasir(standardvariables.arrCandi)
hitungBatu(standardvariables.arrCandi)
hitungAir(standardvariables.arrCandi)

def hargaCandi(arrCandi):
    global candiAda
    global tajMahal
    global biayaTajMahal
    global tajMurah
    global biayaTajMurah
    candiAda = [[0 for cols in range(2)] for rows in range(101)]
    arrCandi = standardvariables.arrCandi
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

            
hargaCandi(standardvariables.arrCandi)

def laporanCandi():
    print(f"Total Candi: {totalCandi}")
    print(f"Total Pasir yang digunakan: {usedPasir}")
    print(f"Total Batu yang digunakan: {usedBatu}")
    print(f"Total Air yang digunakan: {usedAir}")
    print(f"ID Candi Termahal: {tajMahal} (Rp {biayaTajMahal})")
    print(f"ID Candi Termurah: {tajMurah} (Rp {biayaTajMurah})")

# laporanCandi()
