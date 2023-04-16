def jenis_jin(username_jintotal, username_jinpembangun, password_jinpembangun, username_jinpengumpul, password_jinpengumpul):
    from ProgramUtama import length, mappend
    x = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
    tambah = False
    while not (x==1 or x==2):
        print(f'Tidak ada jenis jin bernomor "{x}"')
        x = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
    if x==1:
        print("Memilih jin “Pengumpul”.")
        uname_pengumpul = str(input("Masukkan username jin: "))
        pass_pengumpul = str(input("Masukkan password jin: "))
        j=0
        while j<length(username_jinpengumpul):
            if username_jinpengumpul[j]==uname_pengumpul:
                print(f'Username "{uname_pengumpul}" sudah diambil!')
                uname_pengumpul = str(input("Masukkan username jin: "))
                tambah = False
                j=0
            else:
                tambah = True
            j+=1
        if tambah:
                return mappend(username_jinpengumpul, uname_pengumpul), mappend(username_jintotal, uname_pengumpul), mappend(password_jinpengumpul, pass_pengumpul)
    elif x==2:
        print("Memilih jin Pembangun.")
        uname_pembangun = str(input("Masukkan username jin: "))
        pass_pembangun = str(input("Masukkan password jin: "))
        j=0
        while j<length(username_jinpembangun):
            if username_jinpembangun[j]==uname_pembangun:
                print(f'Username "{uname_pembangun}" sudah diambil!')
                uname_pembangun = str(input("Masukkan username jin: "))
                tambah = False
                j=0
            else:
                tambah = True
                j+=1
        if tambah:
                return mappend(username_jinpembangun, uname_pembangun), mappend(username_jintotal, uname_pembangun), mappend(password_jinpembangun, pass_pembangun)
    else:
        return False
