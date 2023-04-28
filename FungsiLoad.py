import os
import argparse
import csv
arrUser = []
arrBahan=[]
arrCandi=[]
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
        path = 'D:\\kodingan william\\TUBES DASPRO\\contoh\\user.csv'
        rowcount = 0
        for row in open(path):
            rowcount+= 1
        data_user = csv.reader(file, delimiter=";")
        arrUser_sementara = [next(data_user) for i in range (rowcount)]
        arrUser = ['*' for i in range(rowcount-1)]
        for i in range (1,rowcount):
            arrUser[i-1]=arrUser_sementara[i]
        print(arrUser)
        
    with open(path_file_candi, 'r') as file:
        path = 'D:\\kodingan william\\TUBES DASPRO\\contoh\\candi.csv'
        rowcount = 0
        for row in open(path):
            rowcount+= 1
        data_candi = csv.reader(file, delimiter=";")
        arrCandi_sementara = [next(data_candi) for i in range (rowcount)]
        arrCandi = ['*' for i in range(rowcount-1)]
        for i in range (1,rowcount):
            arrUser[i-1]=arrCandi_sementara[i]
        print(arrCandi)


    with open(path_file_bahan, 'r') as file:
        path = 'D:\\kodingan william\\TUBES DASPRO\\contoh\\bahan_bangunan.csv'
        rowcount = 0
        for row in open(path):
            rowcount+= 1
        data_bahan = csv.reader(file, delimiter=";")
        arrBahan_sementara = [next(data_bahan) for i in range (rowcount)]
        arrBahan = ['*' for i in range(rowcount-1)]
        for i in range (1,rowcount):
            arrBahan[i-1]=arrUser_sementara[i]
        print(arrBahan)

    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Prosedur untuk memuat data dari file-file dalam suatu folder.")
    parser.add_argument('nama_folder', type=str, help="Nama folder yang berisi file-file penyimpanan.")
    args = parser.parse_args()
    load_data(args.nama_folder)
