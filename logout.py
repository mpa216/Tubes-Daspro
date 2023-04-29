userAktif = ""

def logout():
    global userAktif
    if userAktif == "" :
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else :
        userAktif = ""
