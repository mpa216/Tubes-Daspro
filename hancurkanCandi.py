import FungsiUtama
import standardvariables

jumlahCandi = FungsiUtama.lengthcandi(standardvariables.arrCandi)
# standardvariables.userAktif = "Roro" --> kalo mo test case. bisa rubah userAktif dari file ini ato dari standardvariables.py (userAKtif = "Roro")
def HancurkanCandi(arrCandi):
    arrCandi = standardvariables.arrCandi
    if (standardvariables.userAktif == "Roro"): 
        id = input("Masukkan ID candi: ")
        for i in range(jumlahCandi):
            if (arrCandi[i][0] == id):
                print(f"Apakah anda ingin menghancurkan candi ID: {id} (Y/N)?")
                jawab = input()
                if (jawab == "Y") or (jawab == "y"):
                    arrCandi[i][0] = str('inf')
                    print("Candi telah berhasil dihancurkan.")
                    break
                elif (jawab == "N") or (jawab == "n"):
                    print("Candi tidak jadi dihancurkan.")
                    break
            else:
                if (i == jumlahCandi-1):
                    print("Tidak ada candi dengan ID tersebut.")
                    break
    else:
        print("Anda tidak memiliki akses untuk fungsi tersebut!") 


# HancurkanCandi(standardvariables.arrCandi) 
# print(standardvariables.arrCandi)
# print(FungsiUtama.lengthcandi(standardvariables.arrCandi))