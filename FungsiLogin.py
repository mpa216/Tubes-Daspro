def login(arruser,useraktif,roleaktif):
        username_login, password_login = str(input("Username: ")), str(input("Password: "))
        while useraktif=="":
            for i in range (0,2): 
                if arruser[i][0]==username_login:
                    if arruser[i][1]==password_login:
                        print(f'Selamat datang, {username_login}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.')
                        useraktif=username_login
                        roleaktif=arruser[i][2]
                    else:
                        kondisi = ("Password salah!")
                        break
                else:
                    kondisi =("Username tidak terdaftar!")
            print(kondisi)
            username_login, password_login = str(input("Username: ")), str(input("Password: "))
        if useraktif!="":
            print(f"Anda telah login dengan username {useraktif}, silahkan lakukan “logout” sebelum melakukan login kembali.  ")
        return
