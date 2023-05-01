procedure HilangkanJin():
  global arrUser
  global arrCandi
  input(jin_hilang)
  kondisi <- False
  i<-1
  iterate (not kondisi) or x<103 do
    if arrUser[i][1] = jin_hilang then
      kondisi <- True
    stop kondisi = True
    i <- i+1
  if kondisi then
    input(hilang)
    while not (hilang="y" or hilang="Y" or hilang="N" or hilang="n") then
      output("Input salah.")
      input(hilang)
    if  hilang='Y' or hilang='y'then
      j <- 3
      repeat 99 times
        arrUser[j] <- arrUser[j+1]
      arrUser[102] <- ['inf','inf','inf']

      j <- 1
      repeat 100 times
        if arrCandi[j][2]=jin_hilang then
          arrCandi[j] <- ['inf','inf','inf','inf','inf']
    else
      output("Jin tidak jadi dihilangkan.")
