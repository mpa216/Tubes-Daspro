                                                          # VERSI        ROMBAK #
arrUser     = [[0 for cols in range (3)] for rows in range(102)] # array 2 dimensi (102 x 3) dengan index 0-99 milik para jin, 100 dimiilki Bandung, 101 dimiliki Roro
# arrUser[x][0], arrUser[x][1], arrUser[x][2] = Username,Role, Password
# Contoh [["Si Cakep","Jin Pembangun","Saya cakep"], ..... , ["Bandung","Antagonist", "Bondowoso"] ,["Roro","Protagonist", "Jonggrang"]]
userAktif = "" # ini berisi username dari pengguna yg aktif, if useraktif == Bandung : ...... elif useraktif == Roro : ....... else #jin : ......
jenisJin = [] # 0: pengumpul 1: pembangun, array ini isinya integer
usernameJinPembangun = [] # array 1 dimensi yang berisi nama-nama jin pembangun yang sudah ditandai dengan index
# Contoh ["Si Cakep", "Si Hebat", ....]
passwordJinPembangun = [] # array 1 dimensi yang berisi password-password jin pembangun yang sudah ditandai dengan index
# Contoh ["Saya cakep", "Saya hebat", ....]
usernameJinPengumpul = [] # array 1 dimensi yang berisi nama-nama jin pengumpul yang sudah ditandai dengan index
# Contoh ["Si Kuat", "Si Gigih", ....]
passwordJinPengumpul = [] # array 1 dimensi yang berisi password-password jin pengumpul yang sudah ditandai dengan index
# Contoh ["Saya kuat", "Saya gigih", ....]
arrCandi    = [[0 for cols in range (5)] for rows in range(100)] # array 2 dimensi (100 x 5) dengan 
# arrCandi[x][0] = id candi, arrCandi[x][1] = Nama jin pembangunnya, arrCandi[x][2] = jumlah pasir/candi, arrCandi[x][3] = jumlah batu/candi, arrCandi[x][4] = jumlah air/candi
# Contoh [[1,"Si Cakep",5,3,4],[2,"Si Hebat",4,3,5], ....]
arrBahan    = [[0 for cols in range (3)] for rows in range(3)] # array 2 dimensi (3 x 3) dengan index 0,1,2 menunjukkan jumlah pasir,batu, air secara berturut
                    # arrBahan[0][0], arrBahan[0][1], arrBahan[0][2] = "Pasir", "Blank", jumlah
# Maksud deskripsi  # arrBahan[1][0], arrBahan[1][1], arrBahan[1][2] = "Batu", "Blank", jumlah
                    # arrBahan[2][0], arrBahan[2][1],arrBahan[2][2] = "Air", "Blank", jumlah
# Contoh [["Pasir","Blank", 40], ["Batu","Blank","30"],["Air","Blank","50"]]

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                          # VERSI SEBELUM ROMBAK #
# # Semua user di akses dengan indeks, misal index 3 adalah jin ifrit, maka seluruh variable dengan indeks 3 adalah milik jin ifrit. 
# # misal passwordjin[3], jenisjin[3], IDcanditiapjin[3]. semua adalah properti dari jin ifrit
# usernamejin = [] # array ini isinya string ini tempat penyimpanan user name jin,
# passwordjin = [] # array ini isinya string
# jenisjin = [] # 0: pengumpul 1: pembangun, array ini isinya integer
# usernameselainlain = ["Bandung", "Roro"]
# passwordselainlain = ["Bondowoso", "Jonggrang"]
# IDcanditiapjin = [] # Ini array 2 dimensi ex. [[12, 31, 32], [2, 1], [100], ...] misal isi string [12, 31, 32] menandakan IDcandi yg dibuat oleh jin dengan index [0], 
# # ini berfungsi untuk mentrack jumlah idcandi yg dibuat oelh tiap jin, mengingat bahwa satu jin dapat membuat lebih dari 1 Candi
# IDcanditotal = [i for i in range(1, 101)] # Ini array 1 dimensi, yg berfungsi untuk menyimpan daftrar data idcandi yg belum dibuat
# IDcandidibuat = [] # ini array 1 deimsi, yg menyimpan data mengenai IDcandi yg sudah taken/dibuat
# bahancanditiapjin = [] # Ini array 2 dimensi ex. [[120, 200, 300], [50, 20 , 200] ...] isinya integer dengan format [[pasir, air, batu]]
# totalbahan = [] # ini array 1 dimensi dengan formar [pasir, air, batu]
# useraktif = "" # ini berisi username dari pengguna yg aktif, if useraktif == Bandung : ...... elif useraktif == Roro : ....... else #jin : ......
