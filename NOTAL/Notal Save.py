procedure save(nama_folder)
    global arrUser
    global arrCandi
    global arrBahan

    if not exists(nama_folder) then
        output("Folder 'nama_folder' tidak ditemukan.")
	   os.mkdir(nama_folder)
    Berhasil menyimpan data di folder

    else
        assign(data_user,'nama_folder\user.csv')
        rewrite(data_user)
        skip <- True
        tulis_header("username;password;role",data_user)
          row traversal (0...101)
            col traversal (0...2)
              if arrUser[row][col]!="inf" then
                if col<2 then
                   write(data_user,str(arrUser[row][col]) + ";")
                else
                   write(data_user,str(arrUser[row][col]))
                skip <- False
            if not skip:
              write(data_user,"\n")
            skip <- True
                   
        assign(data_candi,'nama_folder\candi.csv')
        rewrite(data_candi)
        skip <- True
        tulis_header("id;pembuat;pasir;batu;air",data_candi)
          row traversal (0...99)
            col traversal (0...4)
              if arrCandi[row][col]!="inf" then
                if col<4 then
                   write(data_Candi,str(arrCandi[row][col]) + ";")
                else
                   write(data_Candi,str(arrCandi[row][col]))
                skip <- False
            if not skip:
              write(data_candi,"\n")
            skip <- True
                   
        assign(data_bahan,'nama_folder\bahan_bangunan.csv')
        rewrite(data_user)
        skip <- True
        tulis_header("nama;deskripsi;jumlah",data_bahan)
          row traversal (0...2)
            col traversal (0...2)
              if arrUser[row][col]!="inf" then
                if col<2 then
                   write(data_bahan,str(arrbahan[row][col]) + ";")
                else
                   write(data_bahan,str(arrBahan[row][col]))
                skip <- False
            if not skip:
              write(data_bahan,"\n")
            skip <- True
                   
              
