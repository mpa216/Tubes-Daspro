userAktif = "" #menentukan role user saat ini

def logout(): #mendefinisikan fungsi logout
    global userAktif
    #jika user belum memiliki role, berarti belum login sehingga belum bisa logout
    if userAktif == "" :
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    #jika user sudah memiliki role, maka role tersebut akan dikosongkan
    else :
        userAktif = "" #user berisi string kosong yang berarti sudah berhasil logout
