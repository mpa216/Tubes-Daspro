import random
import FungsiUtama

useraktif = "jin ifrit" # Musti diisin dengan user yg sedang aktif, nama jin ifrit disini hanya contoh

def bangun():
    ids = extract(0, "candi.csv")
    bahans = extract(2, "bahan_bangunan.csv") # 0 = pasir 1 = batu 2 = air
    hapus = extract(0, "hapus.csv")
    for i in range(len(hapus)) :
        hapus[i] = int(hapus[i])
    hapussort = my_sort(hapus)
    pasir = random.randint(1, 5)
    batu = random.randint(1, 5)
    air = random.randint(1, 5)

    pasirreal = int(bahans[0])
    batureal = int(bahans[1])
    airreal = int(bahans[2])

    if pasirreal >= pasir and batureal >= batu and airreal >= air :
        update_bahan((pasirreal - pasir), (batureal - batu), (airreal - air))
        if 100 - len(ids) - 1 == 0 :           
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun: " + str(0))
        else :
            if len(ids) == 0 :
                ygdibuat = 0
            elif len(hapussort) == 0 :
                ygdibuat = (int(my_max(ids)) + 1)
            else :
                ygdibuat = int(hapussort[0])
                hapussort = del_element(hapussort, 0)
                update_hapus(hapussort)

            
            id = str(ygdibuat)
            pembuat = str(useraktif)
            pasir = str(pasir)
            batu = str(batu)
            air = str(air)
            file = open('candi.csv', 'a')
            file.write("\n" + id + "," + pembuat + "," + pasir + "," + batu + "," + air)

            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun: " + str(100 - len(ids) - 1))            

    else :
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
