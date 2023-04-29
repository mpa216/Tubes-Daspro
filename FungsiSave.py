import argparse
import os
def save_data(nama_folder):
    global arrUser
    global arrCandi
    global arrBahan
    #Cek apakah folder ada
    if not os.path.exists(nama_folder):
        print(f"Folder '{nama_folder}' tidak ditemukan.")
    else:
        with open(f"{nama_folder}\\user.csv", "w") as file:
            for row in arrUser:
                for col in row:
                    file.write(str(col) + ";")
                file.write("\n")
            
        with open(f"{nama_folder}\\candi.csv", "w") as file:
            for row in arrCandi:
                for col in row:
                    file.write(str(col) + ";")
                file.write("\n")

        with open(f"{nama_folder}\\bahan_bangunan.csv", "w") as file:
            for row in arrBahan:
                for col in row:
                    file.write(str(col) + ";")
                file.write("\n")
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Prosedur untuk memuat data dari file-file dalam suatu folder.")
    parser.add_argument('nama_folder', type=str, help="Nama folder yang berisi file-file penyimpanan.")
    args = parser.parse_args()
    save_data(args.nama_folder)
