procedure Login()
  global arrUser
  global useraktif
  global roleaktif
  input(username_login, password_login)
  if useraktif!="" then
    output("Anda telah login dengan username tersebut, silahkan lakukan “logout” sebelum melakukan login kembali.")
  while useraktif=="" and roleaktif=="" do
    i <- 1
    iterate
     if arrUser[i][0]=username_login then
        if arrUser[i][1]=password_login then
          kondisi <- ("Selamat datang, Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
          useraktif <- arrUser [i][1]
          roleaktif <- arrUser [i][3]
          stop (arrUser[i][1]=password_login)
        else
          kondisi <- ("Password salah!")
          stop()
        stop (i>=102)
        i <- i +1
      else
        kondisi <- ("Username tidak terdaftar!")
    output(kondisi)
    if kondisi = "Password salah!" or kondisi = "Username tidak terdaftar!" then
      input(username_login, password_login)