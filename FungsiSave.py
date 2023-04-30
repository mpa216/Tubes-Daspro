import os

def tulis_header(header,path):
    with open(path,'w') as f:
        return f.write(f'{header}\n')
    
def save():
    global arrUser
    global arrCandi
    global arrBahan
    #Cek apakah folder ada
    nama_folder = str(input(""))
    path = f'save\\{nama_folder}'

    print("Saving...")
    if not os.path.exists(path):
        print(f"Membuat folder save/{nama_folder}...")
        os.mkdir(path)
    print(f"Berhasil menyimpan data di folder {nama_folder}")
    with open(f"{path}\\user.csv", "a") as file:
        skip = True
        tulis_header("username;password;role",f"{path}\\user.csv")
        for row in range (103):
            for col in range (3):
                if arrUser[row][col]!='inf':
                    if col<2:
                        file.write(str(arrUser[row][col]) + ";")
                    else:
                        file.write(str(arrUser[row][col]))
                    skip = False
            if not skip:
                file.write("\n")
            skip=True
        
    with open(f"{path}\\candi.csv", "a") as file:
        skip = True
        tulis_header("id;pembuat;pasir;batu;air",f"{path}\\candi.csv")
        for row in range (100):
            for col in range (5):
                if arrCandi[row][col]!='inf':
                    if col<4:
                        file.write(str(arrCandi[row][col]) + ";")
                    else:
                        file.write(str(arrCandi[row][col]))
                    skip = False
            if not skip:
                file.write("\n")
            skip=True

    with open(f"{path}\\bahan_bangunan.csv", "a") as file:
        skip = True
        tulis_header("nama;deskripsi;jumlah",f"{path}\\bahan_bangunan.csv")
        for row in range (3):
            for col in range (3):
                if arrBahan[row][col]!='inf':
                    if col<2:
                        file.write(str(arrBahan[row][col]) + ";")
                    else:
                        file.write(str(arrBahan[row][col]))
                    skip = False
            if not skip:
                file.write("\n")
            skip=True
    return
