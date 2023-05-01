procedure HilangkanJin():
  global arrUser
  global arrCandi
  input(jin_hilang)
  kondisi <- False
  i<-0 {indeks pertama = 0}
  iterate
    if arrUser[i][0] = jin_hilang then
      kondisi <- True
    stop (kondisi = True or i=102)
    i <- i+1
  if kondisi then
    input(hilang)
    while not (hilang="y" or hilang="Y" or hilang="N" or hilang="n") then
      output("Input salah.")
      input(hilang)
    if  hilang='Y' or hilang='y'then
      j <- 2
      repeat 99 times
        arrUser[j] <- arrUser[j+1]
        j <- j+1
      arrUser[101] <- ['inf','inf','inf']

      j <- 0
      repeat 100 times
        if arrCandi[j][1]=jin_hilang then
          arrCandi[j] <- ['inf','inf','inf','inf','inf']
          j <- j+1
    else
      output("Jin tidak jadi dihilangkan.")
