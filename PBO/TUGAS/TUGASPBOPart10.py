from os import system 

barang = [
    ["Buku Tulis", 5000,50],
    ["Pulpen", 3000,50],
    ["Pensil", 2000,50],
    ["Penghapus", 500,50]
]


def login():
    print ("======= WELCOME =======")
    username = input("Masukkan Username Anda : ")
    password = input("Masukkan Password Anda : ")
    if username == "Yusuf Sulle" and password == "1103194015":
        return 1
    else : 
        return 0
    
def pilihan():
    print("Pilihan Barang : ")
    print("== Kode  ==  Nama Barang == Harga Satuan == Stok ")
    print("== 001   ==  Buku Tulis  ==     5000     == 50 ")
    print("== 002   ==  Pulpen      ==     3000     == 40 ")
    print("== 003   ==  Pensil      ==     2000     == 100 ")
    print("== 004   ==  Penghapus   ==     500      == 0 ")
    
    pilihan = int(input("Masukkan Kode Barang : ")) - 1 
    
    global nama,harga,stok
    nama = barang[pilihan][0]
    harga= barang[pilihan][1]
    stok = barang[pilihan][2]
    
    if stok == 0:
        return 1
    global jumlah 
    jumlah = int(input("Masukkan Jumlah Barang yang dipilih : "))
    if jumlah > stok :
        return 2


def total():
    diskon = input("Apakah anda memiliki voucher diskon (y/t) : ")
    if diskon == 'y' or diskon == 'Y' :
        print("Selamat anda mendapatkan diskon sebanyak 10%")
        return harga*jumlah*0.9 
    else :
        return jumlah*harga 

def main():
    status = login()
    if status == 0:
        print = ("Mohon Maaf username atau password anda Salah !!")
        system("PAUSE")
        print ("Harap untuk melakukan Login Ulang ! \n")
        main()
    status = pilihan()
    if status == 1 :
        print ("Produk tidak dapat dipilih karena stock saat ini sedang kosong")
        system("PAUSE")
        print ("Harap untuk melakukan Login Ulang ! \n")
        main()
    if status == 2 :
        print ("Stock Tidak mencukupi untuk saat ini !")
        system("PAUSE")
        print ("Harap untuk melakukan Login Ulang ! \n")
        main()
    
main()  
pembelian = total()
print("Total yang anda harus bayar >>> Rp . ",int(pembelian))
print ("Terima Kasih sudah melakukan pembelian di Toko Kami !! ")