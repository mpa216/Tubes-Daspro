import os
import argparse

def mappend_lain_2(arr, c):
    new_arr = [None] * (len_lain(arr) + 2)
    for i in range(len_lain(arr)):
        new_arr[i] = arr[i]
    new_arr[len_lain(arr)] = c
    new_arr[len_lain(arr)+1] = 'inf'
    return new_arr

def len_lain(arr):
    i=0
    sum=0
    while arr[i]!='inf':
        sum+=1
        i+=1
    return sum

def read_csv_file(file_path, delimiter=';'):
    rows = ['inf']
    with open(file_path, 'r') as file:
        line = file.readline()
        while line:
            row = ['inf']
            cell_value = ''
            dalampetik = False
            for i in range (len(line)):
                if line[i] == '"' and not dalampetik:
                    dalampetik = True
                elif line[i] == '"' and dalampetik:
                    dalampetik = False
                elif line[i] == delimiter and not dalampetik:
                    row = mappend_lain_2(row, cell_value)
                    cell_value = ''
                else:
                    cell_value += line[i]
            row = mappend_lain_2(row, cell_value)
            rows = mappend_lain_2(rows, row)
            line = file.readline()
    return rows

def load_data(nama_folder):
    global arrUser
    global arrCandi
    global arrBahan
    #Cek apakah folder ada
    if not os.path.exists(nama_folder):
        print(f"Folder '{nama_folder}' tidak ditemukan.")
        return

    #Load data dari file-file dalam folder
    else:
        with open(f'{nama_folder}\\user.csv', 'r') as file:
            data_user = read_csv_file(file.name, delimiter=";")
            for i in range (1,len_lain(data_user)):
                for j in range (3):
                    arrUser[i-1][j]=data_user[i][j]
            print(arrUser)
            
        with open(f'{nama_folder}\\candi.csv', 'r') as file:
            data_candi = read_csv_file(file.name, delimiter=";")
            for i in range (1,len_lain(data_candi)):
                for j in range (5):
                    arrCandi[i-1][j]=data_candi[i][j]
            print(arrCandi)

        with open(f'{nama_folder}\\bahan_bangunan.csv', 'r') as file:
            data_bahan = read_csv_file(file.name, delimiter=";")
            for i in range (1,len_lain(data_bahan)):
                for j in range (3):
                    arrBahan[i-1][j]=data_bahan[i][j]
            print(arrBahan)
            return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Prosedur untuk memuat data dari file-file dalam suatu folder.")
    parser.add_argument('nama_folder', type=str, help="Nama folder yang berisi file-file penyimpanan.")
    args = parser.parse_args()
    load_data(args.nama_folder)
