import csv
def login(nama_file,useraktif):
    with open(f'{nama_file}',encoding="utf-8") as user:
        file = csv.reader(user, delimiter=";")
        gabungan_data = [next(file) for i in range(3)]
        username_login, password_login = str(input("Username: ")), str(input("Password: "))
        while useraktif=="":
            for i in range (1,3):
                if gabungan_data[i][0]==username_login:
                    if gabungan_data[i][1]==password_login:
                        print(f'Selamat datang, {username_login}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.')
                        return username_login
                    else:
                        kondisi = ("Password salah!")
                        break
                else:
                    kondisi =("Username tidak terdaftar!")
            print(kondisi)
            username_login, password_login = str(input("Username: ")), str(input("Password: "))
        if useraktif!="":
            print(f"Anda telah login dengan username {useraktif}, silahkan lakukan “logout” sebelum melakukan login kembali.  ")
