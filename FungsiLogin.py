import csv
with open("LoginTerakhir.csv",'r') as file:
    file, loginterakhir = csv.reader(file, delimiter=","), [next(file) for i in range(2)]
def login(nama_file,udhlogin):
    with open(f'{nama_file}',encoding="utf-8") as user:
        file = csv.reader(user, delimiter=";")
        gabungan_data = [next(file) for i in range(3)]
        username_login, password_login = str(input("Username: ")), str(input("Password: "))
        while not udhlogin:
            for i in range (1,3):
                if gabungan_data[i][0]==username_login:
                    if gabungan_data[i][1]==password_login:
                        udhlogin = True
                        print(f'Selamat datang, {username_login}!', "\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
                        with open("LoginTerakhir.csv",'w',encoding='utf-8') as datalogin:
                            datalogin.write(f'{username_login},{udhlogin}')
                    else:
                        kondisi = ("Password salah!")
                        break
                else:
                    kondisi =("Username tidak terdaftar!")
            print(kondisi)
            username_login, password_login = str(input("Username: ")), str(input("Password: "))
        if udhlogin:
            print(f"Anda telah login dengan username {loginterakhir[0][0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")
