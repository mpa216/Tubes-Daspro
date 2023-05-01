roleAktif = "" #menentukan role user yang sedang login

def Help(): #Mendefinisikan fungsi help
    
    #command untuk user yang belum login
    notLogin = """1. login - untuk menggunakan akun
    2. exit - untuk keluar dari program dan kembali ke terminal"""
    
    #command yang dapat diakses bandung bondowoso
    bandung = """1. logout - untuk keluar dari akun yang digunakan sekarang
    2. summonjin - untuk memanggila jin
    3. hilangkanjin - untuk menghapus jin
    4. ubahtipejin - untuk mengubah tipe jin
    5. batchkumpul/bangun - untuk mengerahkan seluruh pasukan jin untuk mengumpulkan bahan atau pembangun
    6. ambillaporanjin - untuk mengambil laporan jin atas kinerja para jin
    7. laporancandi - untuk mengambil laporan candi untuk mengetahui progress pembangunan candi
    8. exit - untuk keluar dari program dan kembali ke terminal"""
    
    #command yang dapat diakses roro jonggrang
    roro = """1. logout - untuk keluar dari akun yang digunakan sekarang
    2. hancurkancandi - untuk menghancurkan candi yang tersedia
    3. ayamberkokok - untuk menyelesaikan permainan dengan memalsukan pagi hari
    4. exit - untuk keluar dari program dan kembali ke terminal"""
    
    #command yang dapat diakses jin pengumpul
    jinPengumpul = """1. logout - untuk keluar dari akun yang digunakan sekarang
    2. kumpul - untuk mengumpulkan candi
    3. exit - untuk keluar dari program dan kembali ke terminal"""
    
    #command yang dapat diakses jin pembangun
    jinPembangun = """1. logout - untuk keluar dari akun yang digunakan sekarang
    2. bangun - untuk membangun candi
    3. exit - untuk keluar dari program dan kembali ke terminal"""
    
    #jika user belum memiliki role, berarti belum login sehingga print command notLogin
    if roleAktif == "":
        print("===========HELP===========")
        print(notLogin)
    else:
        if roleAktif == "bandung_bondowoso": #jika role user adalah bandung bondowoso, maka print command bandung
            print("===========HELP===========")
            print(bandung)
        elif roleAktif == "roro_jonggrang": #jika role user adalah roro jonggrang, maka print command roro
            print("===========HELP===========")
            print(roro)
        elif roleAktif == "jin_pengumpul": #jika role user adalah jin pengumpul, maka print command jinPengumpul
            print("===========HELP===========")
            print(jinPengumpul)
        elif roleAktif == "jin_pembangun": #jika role user adalah jin pembangun, maka print command jinPembangun
            print("===========HELP===========")
            print(jinPembangun)
