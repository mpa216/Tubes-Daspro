arrCandi    = [[str("inf") for cols in range (5)] for rows in range(100)] # array 2 dimensi (100 x 5) dengan 
# arrCandi[x][0] = id candi, arrCandi[x][1] = Nama jin pembangunnya, arrCandi[x][2] = jumlah pasir/candi, arrCandi[x][3] = jumlah batu/candi, arrCandi[x][4] = jumlah air/candi
# Contoh [[1,"Si Cakep",5,3,4],[2,"Si Hebat",4,3,5], ....]
arrBahan = [['pasir', 'blank', 'inf'], ['batu', 'blank', 'inf'], ['air', 'blank', 'inf']]
# arrBahan    = [[str("inf") for cols in range (3)] for rows in range(3)] # array 2 dimensi (3 x 3) dengan index 0,1,2 menunjukkan jumlah pasir,batu, air secara berturut
                    # arrBahan[0][0], arrBahan[0][1], arrBahan[0][2] = "Pasir", "Blank", jumlah
# Maksud deskripsi  # arrBahan[1][0], arrBahan[1][1], arrBahan[1][2] = "Batu", "Blank", jumlah
                    # arrBahan[2][0], arrBahan[2][1],arrBahan[2][2] = "Air", "Blank", jumlah
# Contoh [["Pasir","Blank", 40], ["Batu","Blank","30"],["Air","Blank","50"]]
arrUser     = [[str("inf") for cols in range (3)] for rows in range(102)] # array 2 dimensi (102 x 3) dengan index 0-99 milik para jin, 100 dimiilki Bandung, 101 dimiliki Roro
# arrUser[x][0], arrUser[x][1], arrUser[x][2] = Username,Role, Password
# Contoh [["Si Cakep","Jin Pembangun","Saya cakep"], ..... , ["Bandung","Antagonist", "Bondowoso"] ,["Roro","Protagonist", "Jonggrang"]]
userAktif = "" # ini berisi username dari pengguna yg aktif, if useraktif == Bandung : ...... elif useraktif == Roro : ....... else #jin : ......
roleAktif = ""

arrUser = [["Bondowoso","cintaroro","bandung_bondowoso"], ["Roro","gasukabondo","roro_jonggrang"]]

def login():
        global arrUser
        global userAktif
        global roleAktif

        while userAktif=="":
            username_login, password_login = str(input("Username: ")), str(input("Password: "))
            for i in range (0,2):
                if arrUser[i][0]==username_login:
                    if arrUser[i][1]==password_login:
                        print(f'Selamat datang, {username_login}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.')
                        userAktif = str(username_login)
                        roleAktif = str(arrUser[i][2])
                        return
                        
                    else:
                        kondisi = ("Password salah!")
                        break
                else:
                    kondisi =("Username tidak terdaftar!")
            print(kondisi)
        if userAktif!="":
            print(f"Anda telah login dengan username {userAktif}, silahkan lakukan “logout” sebelum melakukan login kembali.  ")
            return

# Untuk testing
# gaming = True
# while gaming :
#     command = input("command: ")
#     if command == "login" :
#         login()
#         print(userAktif)
#         print(roleAktif)
#     elif command == "logout" :
#         userAktif = ""
#         roleAktif = ""
