def UbahTipeJin():
    global arrUser
    ada = False
    jinygdiubah = str(input("Masukkan username jin :"))
    for i in range (2,103):
        if arrUser[i][0]==jinygdiubah:
            ada = True
            break
    if ada:
        if arrUser[i][2]=="Pembangun":
            tipe = "Pengumpul"
        else:
            tipe = "Pembangun"
        masukan = str(input(f'Jin ini bertipe {arrUser[i][2]}. Yakin ingin mengubah ke tipe {tipe} (Y/N)? '))
        if masukan=='Y' or masukan=='y':
            arrUser[i][2]=tipe
            print("Jin telah berhasil diubah.")
        elif masukan=="N" or masukan=="n":
            print("Jin tidak jadi diubah.")
    else:
        print("Tidak ada jin dengan username tersebut.")
    return
