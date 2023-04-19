# Semua user di akses dengan indeks, misal index 3 adalah jin ifrit, maka seluruh variable dengan indeks 3 adalah milik jin ifrit. 
# misal passwordjin[3], jenisjin[3], IDcanditiapjin[3]. semua adalah properti dari jin ifrit
usernamejin = [] # array ini isinya string ini tempat penyimpanan user name jin,
passwordjin = [] # array ini isinya string
jenisjin = [] # 0: pengumpul 1: pembangun, array ini isinya integer
usernameselainlain = ["Bandung", "Roro"]
passwordselainlain = ["Bondowoso", "Jonggrang"]
IDcanditiapjin = [] # Ini array 2 dimensi ex. [[12, 31, 32], [2, 1], [100], ...] misal isi string [12, 31, 32] menandakan IDcandi yg dibuat oleh jin dengan index [0], 
# ini berfungsi untuk mentrack jumlah idcandi yg dibuat oelh tiap jin, mengingat bahwa satu jin dapat membuat lebih dari 1 Candi
IDcanditotal = [i for i in range(1, 101)] # Ini array 1 dimensi, yg berfungsi untuk menyimpan daftrar data idcandi yg belum dibuat
IDcandidibuat = [] # ini array 1 deimsi, yg menyimpan data mengenai IDcandi yg sudah taken/dibuat
bahancanditiapjin = [] # Ini array 2 dimensi ex. [[120, 200, 300], [50, 20 , 200] ...] isinya integer dengan format [[pasir, air, batu]]
totalbahan = [] # ini array 1 dimensi dengan formar [pasir, air, batu]
useraktif = "" # ini berisi username dari pengguna yg aktif, if useraktif == Bandung : ...... elif useraktif == Roro : ....... else #jin : ......
