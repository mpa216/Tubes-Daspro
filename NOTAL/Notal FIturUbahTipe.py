procedure UbahTipe()
  global arrUser
  ada <- False
  input(jinygdiubah)
  i <- 1
  while (not ada) or i<103 do
    if arrUser[i][1] = jinygdiubah then
      ada <- True
    i <- i+1
  if ada then
    if arrUser[i-1][3] = "jin_pembangun" then
      tipe = "jin_pengumpul"
    else
      tipe = "jin_pembangun"
    input(masukan)
    if masukan='Y' or masukan='y'then
      arrUser[i-1][3]<-tipe
      output("Jin telah berhasil diubah.")
    else if masukan=="N" or masukan=="n" then
      output("Jin tidak jadi diubah.")
  else
    output("Tidak ada jin dengan username tersebut.")