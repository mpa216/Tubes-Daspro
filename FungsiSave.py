import argparse
import os
def tulis_header(header,path):
    with open(path,'w') as f:
        return f.write(f'{header};\n')
    
def save(nama_folder):
    global arrUser
    global arrCandi
    global arrBahan
    #Cek apakah folder ada
    if not os.path.exists(nama_folder):
        print(f"Folder '{nama_folder}' tidak ditemukan.")
    #Load data dari file-file dalam folder
    else:
        with open(f"{nama_folder}\\user.csv", "a") as file:
            skip = True
            tulis_header("username;password;role",f"{nama_folder}\\user.csv")
            for row in range (102):
                for col in range (3):
                    if arrUser[row][col]!='inf':
                        file.write(str(arrUser[row][col]) + ";")
                        skip = False
                if not skip:
                    file.write("\n")
                skip=True
            
        with open(f"{nama_folder}\\candi.csv", "a") as file:
            skip = True
            tulis_header("id;pembuat;pasir;batu;air",f"{nama_folder}\\candi.csv")
            for row in range (100):
                for col in range (5):
                    if arrCandi[row][col]!='inf':
                        file.write(str(arrCandi[row][col]) + ";")
                        skip = False
                if not skip:
                    file.write("\n")
                skip=True
    
        with open(f"{nama_folder}\\bahan_bangunan.csv", "a") as file:
            skip = True
            tulis_header("nama;deskripsi;jumlah",f"{nama_folder}\\bahan_bangunan.csv")
            for row in range (3):
                for col in range (3):
                    if arrBahan[row][col]!='inf':
                        file.write(str(arrBahan[row][col]) + ";")
                        skip = False
                if not skip:
                    file.write("\n")
                skip=True
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Prosedur untuk menyimpan data ke file-file dalam suatu folder.")
    parser.add_argument('nama_folder', type=str, help="Nama folder yang berisi file-file penyimpanan.")
    args = parser.parse_args()
    save(args.nama_folder)
