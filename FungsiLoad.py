import os
import argparse

def mappend_lain(arr, c):
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
def len_matriks(arr):
    i=0
    sum=0
    while arr[i][0]!='inf':
        sum+=1
        i+=1
    return

def read_csv_file(file_path, delimiter=';'):
    rows = ['inf']
    with open(file_path, 'r') as file:
        line = file.readline()
        while line:
            row = ['inf']
            cell_value = ''
            inside_quotes = False
            for char in line:
                if char == '"' and not inside_quotes:
                    inside_quotes = True
                elif char == '"' and inside_quotes:
                    inside_quotes = False
                elif char == delimiter and not inside_quotes:
                    row = mappend(row, cell_value)
                    cell_value = ''
                else:
                    cell_value += char
            row = mappend(row, cell_value)
            rows = mappend(rows, row)
            line = file.readline()
    return rows

def load_data(nama_folder):
    global arrUser
    global arrCandi
    global arrBahan
    #Cek apakah folder ada
    if not os.path.exists(nama_folder):
        print(f"Folder '{nama_folder}' tidak ditemukan.")

    #Load data dari file-file dalam folder
    else:
        with open(f'{nama_folder}\\user.csv', 'r') as file:
            data_user = read_csv_file(file.name, delimiter=";")
            for i in range (1,len_lain(data_user)):
                for j in range (3):
                    arrUser[i-1][j-1]=data_user[i][j]
            print(arrUser)
            
        with open(f'{nama_folder}\\candi.csv', 'r') as file:
            data_candi = read_csv_file(file.name, delimiter=";")
            for i in range (1,len_lain(data_candi)):
                for j in range (5):
                    arrCandi[i-1][j-1]=data_candi[i][j]
            print(arrCandi)

        with open(f'{nama_folder}\\bahan_bangunan.csv', 'r') as file:
            data_bahan = read_csv_file(file.name, delimiter=";")
            for i in range (1,len_lain(data_bahan)):
                for j in range (3):
                    arrBahan[i-1][j-1]=data_bahan[i][j]
            print(arrBahan)
        return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Prosedur untuk memuat data dari file-file dalam suatu folder.")
    parser.add_argument('nama_folder', type=str, help="Nama folder yang berisi file-file penyimpanan.")
    args = parser.parse_args()
    load_data(args.nama_folder)
