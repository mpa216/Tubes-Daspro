def login():
        global arrUser
        global useraktif
        global roleaktif
        username_login, password_login = str(input("Username: ")), str(input("Password: "))
        if useraktif!="":
            print(f"Anda telah login dengan username {useraktif}, silahkan lakukan “logout” sebelum melakukan login kembali.  ")
        while useraktif=="" and roleaktif=="":
            for i in range (0,2): 
                if arrUser[i][0]==username_login:
                    if arrUser[i][1]==password_login:
                        kondisi = (f'Selamat datang, {username_login}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.')
                        useraktif=arrUser[i][0]
                        roleaktif=arrUser[i][2]
                        break
                    else:
                        kondisi = ("Password salah!")
                        break
                else:
                    kondisi =("Username tidak terdaftar!")
            print(kondisi)
            if kondisi == "Password salah!" or kondisi == "Username tidak terdaftar!":
                username_login, password_login = str(input("Username: ")), str(input("Password: "))
        return
