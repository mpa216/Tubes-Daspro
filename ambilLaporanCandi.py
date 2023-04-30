from FungsiUtama import lengthcandi

arrCandi    = [[str("inf") for cols in range (5)] for rows in range(100)] # array 2 dimensi (100 x 5) dengan 


# arrCandi[0][0] = "1"
# arrCandi[0][2],arrCandi[0][3],arrCandi[0][4] = "1","2","3"

# arrCandi[3][0] = "4"
# arrCandi[3][2],arrCandi[3][3],arrCandi[3][4] = "165","166","112"

# arrCandi[4][0] = "5"
# arrCandi[4][2],arrCandi[4][3],arrCandi[4][4] = "1650","166","1212"

totalCandi = lengthcandi(arrCandi)

def laporanCandi():
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
laporanCandi()

