import argparse
import os
def save_data(nama_folder):
    global arrUser
    global arrCandi
    global arrBahan
    #Cek apakah folder ada
    if not os.path.exists(nama_folder):
        print(f"Folder '{nama_folder}' tidak ditemukan.")
    #Load data dari file-file dalam folder
    else:
        with open(f"{nama_folder}\\user.csv", "w") as file:
            skip = True
            header = ["username","password","role"]
            for col in range (3):
                file.write(str(header[col]) + ";")
            file.write("\n")
            for row in range (103):
                for col in range (3):
                    if arrUser[row][col]!='inf':
                        file.write(str(arrUser[row][col]) + ";")
                        skip = False
                if not skip:
                    file.write("\n")
                skip=True
            
        with open(f"{nama_folder}\\candi.csv", "w") as file:
            skip = True
            header = ["id","pembuat","pasir","batu","air"]
            for col in range (5):
                file.write(str(header[col]) + ";")
            file.write("\n")
            for row in range (100):
                for col in range (5):
                    if arrCandi[row][col]!='inf':
                        file.write(str(arrCandi[row][col]) + ";")
                        skip = False
                if not skip:
                    file.write("\n")
                skip=True
    
        with open(f"{nama_folder}\\bahan_bangunan.csv", "w") as file:
            skip = True
            header = ["nama","deskripsi","jumlah"]
            for col in range (3):
                file.write(str(header[col]) + ";")
            file.write("\n")
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
    parser = argparse.ArgumentParser(description="Prosedur untuk memuat data dari file-file dalam suatu folder.")
    parser.add_argument('nama_folder', type=str, help="Nama folder yang berisi file-file penyimpanan.")
    args = parser.parse_args()
    save_data(args.nama_folder)