
                                                          # VERSI        ROMBAK #
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

from FungsiUtama import lengthcandi

# arrCandi[0][0] = 1 
#                     #--> kalo mo test case
# arrCandi[1][0] = 2    

# userAktif = "Roro" #--> kalo mo test case

jumlahCandi = lengthcandi(arrCandi)
def ayam_berkokok ():
    if (userAktif == "Roro"):
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
        print("Anda tidak memiliki akses untuk fungsi tersebut!") 

# ayam_berkokok() # --> jika mau test cse


