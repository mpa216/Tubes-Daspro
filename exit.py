import sys
import FungsiUtama

def exit():
    salah = True
    while salah :
        simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if simpan == "y" : 
            save()
            sys.exit()
        elif simpan == "n" :
            sys.exit()
