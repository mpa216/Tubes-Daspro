Notasi Algoritmik (Fitur SummonJin)
Procedure tambah_jin()
{Merupakan procedure yang dapat mengubah variabel global, yaitu arrUser, dengan “menambahkan” suatu elemen.
I.S.: global arrUser terdefinisi
F.S: dapat “menambah” elemen dalam arrUser}
Kamus Lokal
x : integer
tambah : boolean
tipe, username_jin, password_jin : string
Algoritma
  global arrUser
  output("Jenis jin yang dapat dipanggil:")
  output(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
  output(" (2) Pembangun - Bertugas membangun candi")
  input(x) {Masukkan nomor jenis jin yang ingin dipanggil:}
  tambah <- False
  while not (x=1 or x=2) do
    input(x) {Masukkan nomor jenis jin yang ingin dipanggil:}
  If length(arrUser)<102 then
    while not tambah do
      If x=1 then
        tipe <- “Pengumpul”
        role <- "jin_pengumpul"
      else
        tipe <- “jin_pembangun”
        role <- "jin_pembangun"
      output(“Memilih Jin ”+tipe)
      Input(username_jin,password_jin)
      i <- 0 {indeks pertama 0}
      iterate
        if arrUser[i][0]=username_jin {indeks pertama dari suatu array adalah 1} then
            output("Username sudah diambil")
            tambah <- False
          else
            tambah <-True
        stop (i>102)
        i <- i+1
        stop arrUser[i][0]=username_jin {indeks pertama dari suatu array adalah 1}
    if tambah then
      arrUser = append_lain(arrUser,[username_jin,password_jin,tipe])
  else
    output("Jin sudah Penuh")
