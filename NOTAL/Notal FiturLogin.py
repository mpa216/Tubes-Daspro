procedure Login()
  global arrUser
  global useraktif
  global roleaktif
  global cobalogin
  udhlogin <- False
  while not udhlogin do
    i <- 1 {indeks pertama array =1}
    input(username_login,password_login)
    iterate
     if arrUser[i][1]=username_login then
        if arrUser[i][2]=password_login then
          cobalogin <- cobalogin + 1
          if cobalogin>1 then
            kondisi <- ("Logout terlebih dahulu")
          else
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
