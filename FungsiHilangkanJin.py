def HilangkanJin():
    global arrUser
    global arrCandi

    jin_hilang = str(input("Masukkan username jin : "))
    kondisi= False
    for i in range (2,102):
        if arrUser[i][0]==jin_hilang:
            kondisi = True
            break
    if kondisi:
        hilang = str(input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? "))
        while not (hilang=="y" or hilang=="Y" or hilang=="N" or hilang=="n"):
            print("Input salah.")
            hilang = str(input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? "))
        if hilang=='Y' or hilang=='y':
            for j in range (2,101):
                arrUser[j]=arrUser[j+1]
            arrUser[101] = ['inf','inf','inf']
            for j in range (100):
                if arrCandi[j][1]==jin_hilang:
                    arrCandi[j]=['inf','inf','inf','inf','inf']
        elif hilang=="N" or hilang=="n":
            print("Jin tidak jadi dihilangkan.")
        
