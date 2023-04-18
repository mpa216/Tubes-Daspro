from ProgramUtama  import length

arrCandi = [0 for i in range (103)] # arrCandi array berisi kumpulan candi, asumsi sudah penuh

arrCandi[0] = 1 # hanya sebagai test case, tidak akan dimasukkan di versi akhir

jumlahCandi = length(arrCandi) # sebagai variabel panjang array candi
useraktif = "Jonggrang" # test case jika user jonggrang

def HancurkanCandi(arrCandi):
    if (useraktif == "Jonggrang"): 
        id = int(input("Masukkan ID candi: "))
        for i in range(jumlahCandi):
            if (arrCandi[i] == id):
                print(f"Apakah anda ingin menghancurkan candi ID: {id} (Y/N)?")
                jawab = input()
                if (jawab == "Y") or (jawab == "y"):
                    arrCandi[i] = float('inf')
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
        print("Anda tidak memiliki akses untuk fungsi tersebut!") # output jika user lain mencoba memakai fungsi tersebut


HancurkanCandi(arrCandi) #test case

print(arrCandi) # test case untuk mengecek kondisi array terbaru
print(length(arrCandi)) # test case untuk mengecek panjang array 
