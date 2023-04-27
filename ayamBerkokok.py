import FungsiUtama
import standardvariables

jumlahCandi = FungsiUtama.lengthcandi(standardvariables.arrCandi)
# standardvariables.userAktif = "Roro" --> jika mau test case
def ayam_berkokok (arrCandi):
    # global standardvariables.arrCandi
    if (standardvariables.userAktif == "Roro"):
        if (jumlahCandi) < (100):
            print("Kukuruyuk.. Kukuruyuk.. \n")
            print(f"Jumlah Candi: {jumlahCandi} \n ")
            print("Selamat, Roro Jonggrang memenangkan permainan! \n")
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")
            exit()
        else:
            print("Kukuruyuk.. Kukuruyuk.. \n")
            print(f"Jumlah Candi: {jumlahCandi} \n ")
            print("Yah, Bandung Bondowoso memenangkan permainan!")
            exit()
    else:
        print("Anda tidak memiliki akses untuk fungsi tersebut!") 

# ayam_berkokok(standardvariables.arrCandi) --> jika mau test cse


