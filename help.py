from login import *
notLogin = """1. login - untuk menggunakan akun
2. exit - untuk keluar dari program dan kembali ke terminal"""
bandung = """1. logout - untuk keluar dari akun yang digunakan sekarang
2. summonjin - untuk memanggila jin
3. hilangkanjin - untuk menghapus jin
4. ubahtipejin - untuk mengubah tipe jin
5. batchkumpul/bangun - untuk mengerahkan seluruh pasukan jin untuk mengumpulkan bahan atau pembangun
6. ambillaporanjin - untuk mengambil laporan jin atas kinerja para jin
7. laporancandi - untuk mengambil laporan candi untuk mengetahui progress pembangunan candi
8. exit - untuk keluar dari program dan kembali ke terminal"""
roro = """1. logout - untuk keluar dari akun yang digunakan sekarang
2. hancurkancandi - untuk menghancurkan candi yang tersedia
3. ayamberkokok - untuk menyelesaikan permainan dengan memalsukan pagi hari
4. exit - untuk keluar dari program dan kembali ke terminal"""
jinPengumpul = """1. logout - untuk keluar dari akun yang digunakan sekarang
2. kumpul - untuk mengumpulkan candi
3. exit - untuk keluar dari program dan kembali ke terminal"""
jinPembangun = """1. logout - untuk keluar dari akun yang digunakan sekarang
2. bangun - untuk membangun candi
3. exit - untuk keluar dari program dan kembali ke terminal"""

def Help():
    if udhlogin == False:
        print("===========HELP===========")
        print(notLogin)
    elif udhlogin == True:
        if username_login == "Bandung Bondowoso":
            print("===========HELP===========")
            print(bandung)
        elif username_login == "Roro Jongrang":
            print("===========HELP===========")
            print(roro)
        elif username_login == "Jin Pengumpul":
            print("===========HELP===========")
            print(jinPengumpul)
        elif username_login == "Jin Pembangun":
            print("===========HELP===========")
            print(jinPembangun)
        