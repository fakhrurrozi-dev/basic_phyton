listnama = []
listtelepon = []
n = 0

print("------Selamat Datang------")

while(True):

    print("---Menu---")
    print("1. Daftar Kontak ")
    print("2. Tambah Kontak ")
    print("3. Keluar        ")

    menu = int(input("pilih menu :"))

    if(menu==1):
        print("Daftar Kontak")
        for i in range (0, n):
          print(str(i+1) + "." + "Nama : " + str(listnama[i]))
          print(" No telepon :" + str(listtelepon[i]))
    elif (menu==2):
        print("Tambah Kontak")
        nama = str(input("Nama :"))
        listnama.append(nama)
        telepon = int(input("No Telepon :"))
        listtelepon.append(telepon)
        print("Kontak berhasil ditambahkan")
        n += 1
    elif (menu==3):
        break
    else:
        print("Menu tidak tersedia")


    print("Program selesai sampai jumpa!")          