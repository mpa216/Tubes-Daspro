from ProgramUtama import append_lain
def jenis_jin(arrUser):
    x = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
    tambah = False
    while not (x==1 or x==2):
        print(f'Tidak ada jenis jin bernomor "{x}"')
        x = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
    username_jin = str(input("Masukkan username jin: "))
    password_jin = str(input("Masukkan password jin: "))
    if x==1:
        print("Memilih jin “Pengumpul”.")
        for i in range (2,103):
            if arrUser[i][0]==username_jin:
                print(f'Username "{username_jin}" sudah diambil!')
                username_jin = str(input("Masukkan username jin: "))
                tambah = False
                break
            else:
                tambah = True
        if tambah:
            arrUser = append_lain(arrUser,[username_jin,password_jin,'Pengumpul'])
    elif x==2:
        print("Memilih jin Pembangun.")
        for i in range (2,103):
            if arrUser[i][0]==username_jin:
                print(f'Username "{username_jin}" sudah diambil!')
                username_jin = str(input("Masukkan username jin: "))
                tambah = False
                break
            else:
                tambah = True
        if tambah:
            arrUser = append_lain(arrUser,[username_jin,password_jin,'Pembangun'])
    return
