from ProgramUtama  import length

jumlahCandi = length(arrCandi)
def HancurkanCandi(arrCandi):
    id = int(input("Masukkan ID candi: "))
    for i in range(jumlahCandi):
        if (arrCandi[i] == id):
            print(f"Apakah anda ingin menghancurkan candi ID: {id} (Y/N)?")
            jawab = input()
            if (jawab == "Y"):
                arrCandi[i] = float('inf')
                print("Candi telah berhasil dihancurkan.")
            elif (jawab == "N"):
                print("Candi tidak jadi dihancurkan.")
        else:
            if (i == jumlahCandi-1):
                print("Tidak ada candi dengan ID tersebut.")

