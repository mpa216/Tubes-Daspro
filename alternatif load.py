import os
import argparse

def read_csv_file(file_path, delimiter=';'):
    rows = []
    with open(file_path, 'r') as file:
        line = file.readline()
        while line:
            row = []
            cell_value = ''
            inside_quotes = False
            for char in line:
                if char == '"' and not inside_quotes:
                    inside_quotes = True
                elif char == '"' and inside_quotes:
                    inside_quotes = False
                elif char == delimiter and not inside_quotes:
                    row.append(cell_value)
                    cell_value = ''
                else:
                    cell_value += char
            row.append(cell_value)
            rows.append(row)
            line = file.readline()
    return rows


import os
import argparse
arrUser = []
arrBahan=[]
arrCandi=[]
def load_data(nama_folder):
    global arrUser
    global arrCandi
    global arrBahan
    #Cek apakah folder ada
    if not os.path.exists(nama_folder):
        print("Folder '{nama_folder}' tidak ditemukan.")

    #Load data dari file-file dalam folder
    else:
        with open(f'{nama_folder}\\user.csv', 'r') as file:
            rowcount = 0
            for row in open(f'{nama_folder}\\user.csv'):
                rowcount+= 1
            data_user = read_csv_file(file, delimiter=";")
            arrUser_sementara = [next(data_user) for i in range (rowcount)]
            arrUser = ['*' for i in range(rowcount-1)]
            for i in range (1,rowcount):
                arrUser[i-1]=arrUser_sementara[i]
            print(arrUser)
            
        with open(f'{nama_folder}\\candi.csv', 'r') as file:
            rowcount = 0
            for row in open(f'{nama_folder}\\candi.csv'):
                rowcount+= 1
            data_candi = read_csv_file(file, delimiter=";")
            arrCandi_sementara = [next(data_candi) for i in range (rowcount)]
            arrCandi = ['*' for i in range(rowcount-1)]
            for i in range (1,rowcount):
                arrUser[i-1]=arrCandi_sementara[i]
            print(arrCandi)


        with open(f'{nama_folder}\\bahan_bangunan.csv', 'r') as file:
            rowcount = 0
            for row in open(f'{nama_folder}\\bahan_bangunan.csv'):
                rowcount+= 1
            data_bahan = read_csv_file(file, delimiter=";")
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