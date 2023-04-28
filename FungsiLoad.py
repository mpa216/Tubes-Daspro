import os
import argparse
import csv
def load_data(nama_folder):
    global arrUser
    global arrCandi
    global arrBahan
    #Cek apakah folder ada
    if not os.path.exists(nama_folder):
        raise ValueError("Folder '{nama_folder}' tidak ditemukan.")

    #Load data dari file-file dalam folder
    nama_file = ["user.csv","bahan_bangunan.csv", "candi.csv"]
    path_file_user = os.path.join(nama_folder, nama_file[0])
    path_file_bahan = os.path.join(nama_folder, nama_file[1])
    path_file_candi = os.path.join(nama_folder, nama_file[2])
    with open(path_file_user, 'r') as file:
        data_user = csv.reader(file, delimiter=";")
        arrUser = [next(data_user) for i in range(1,103)]
        
    with open(path_file_candi, 'r') as file:
        data_candi = file.read()
        arrCandi = [next(data_candi) for i in range(1,102)]


    with open(path_file_bahan, 'r') as file:
        data_bahan = file.read()
        arrBahan = [next(data_bahan) for i in range(1,4)]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Prosedur untuk memuat data dari file-file dalam suatu folder.")
    parser.add_argument('nama_folder', type=str, help="Nama folder yang berisi file-file penyimpanan.")
    args = parser.parse_args()
    load_data(args.nama_folder)
