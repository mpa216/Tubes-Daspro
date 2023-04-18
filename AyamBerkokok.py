from ProgramUtama  import length
arrCandi = [0 for i in range (103)] # arrCandi array berisi kumpulan candi, asumsi sudah penuh

useraktif = "Jonggrang" # test case jika user jonggrang

jumlahCandi = length(arrCandi)
def ayam_berkokok (arrCandi):
    if (useraktif == "Jonggrang"):
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
    else:
        print("Anda tidak memiliki akses untuk fungsi tersebut!") # output jika user lain mencoba memakai fungsi tersebut



ayam_berkokok(arrCandi) # test case jika array sudah 100 atau lebih
