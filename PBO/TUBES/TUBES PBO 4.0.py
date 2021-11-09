#Kelas_Pertama
class Cells :
    def __init__(self,nama,umur,noHp,pilih):
        self.nama = nama
        self.umur = umur
        self.noHp = noHp
        self.pilih = pilih
        
    def Person_info(self):
        print("|| Nama      : ", self.nama)
        print("|| Umur      : ", self.umur , " Tahun")
        print("|| No Hp     : ", self.noHp)
        
    def tampilan(self):
        if self.pilih == 1 :
            print(f"\nPilihan {self.nama} adalah Nomor 1 (IPHONE) ")
            print("Berikut adalah list untuk Handphone merek Iphone")
            print("-- TAMPILAN UNTUK MEREK HANDPHONE IPHONE -- ")
            print("||============================||")
            print("||    NAMA            == KODE ||")
            print("||============================||")
            print("||  IphoneX           ==  A1  ||")
            print("||  IphoneXs          ==  A2  ||")
            print("||  IphoneXs MAX      ==  A3  ||")
            print("||  Iphone11          ==  A4  ||")
            print("||  Iphone11 Pro      ==  A5  ||")
            print("||  Iphone11 Pro Max  ==  A6  ||")
            print("||  Iphone12          ==  A7  ||")
            print("||  Iphone12 Mini     ==  A8  ||")
            print("||  Iphone12 Pro      ==  A9  ||")
            print("||  Iphone12 Pro Max  ==  A10 ||")
            print("||============================||")
        elif self.pilih == 2 :
            print(f"\nPilihan {self.nama} adalah Nomor 2 (SAMSUNG) ")
            print("Berikut adalah list untuk Handphone merek Samsung") 
            print("-- TAMPILAN UNTUK MEREK HANDPHONE SAMSUNG -- ")
            print("||==================================||")
            print("||     NAMA                 == KODE ||")
            print("||==================================||")
            print("||  GalaxyS10 Silver        ==  B1  ||")
            print("||  GalaxyS10 Gold          ==  B2  ||")
            print("||  GalaxyS10+ Silver       ==  B3  ||")
            print("||  GalaxyS10+ Gold         ==  B4  ||")
            print("||  GalaxyS10e              ==  B5  ||")
            print("||  GalaxyS20 FE            ==  B6  ||")
            print("||  GalaxyS20               ==  B7  ||")
            print("||  GalaxyS20+              ==  B8  ||")
            print("||  GalaxyS20 ULTRA         ==  B9  ||")
            print("||  GalaxyS20+ BTS Edition  ==  B10 ||") 
            print("||==================================||")

#Kelas_Kedua
class beli():
    def __init__(self,pelanggan,kode):
        self.pelanggan = pelanggan
        self.kode = kode
    def sortir(self):
        self.loop = True
        while self.loop == True :
            if self.kode == 'A1' or self.kode =='a1' :
                print("||  NAMA     ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  IphoneX             64 GB     Rp. 9.000.000   ==  A1  ||")
                self.nama_hp = "Iphone X"
                self.kapasitas = "64 GB"
                self.harga = 9000000
                self.tes = True
                self.loop = False
            elif self.kode == 'A2' or self.kode =='a2':
                print("||  NAMA     ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  IphoneXs            64 GB     Rp. 9.500.000   ==  A2  ||")
                self.nama_hp = "Iphone Xs"
                self.kapasitas = "64 GB"
                self.harga = 9500000
                self.tes = True
                self.loop = False
            elif self.kode == 'A3' or self.kode =='a3' :
                print("||  NAMA     ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  IphoneXs MAX        64 GB     Rp. 10.000.000  ==  A3  ||")
                self.nama_hp = "Iphone Xs Max"
                self.kapasitas = "64 GB"
                self.harga = 10000000
                self.tes = True
                self.loop = False
            elif self.kode == 'A4' or self.kode =='a4' :
                print("||  NAMA     ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  Iphone11            64 GB     Rp. 12.690.000  ==  A4  ||")
                self.nama_hp = "Iphone 11"
                self.kapasitas = "64 GB"
                self.harga = 12690000
                self.tes = True
                self.loop = False
            elif self.kode == 'A5' or self.kode =='a5' :
                print("||  NAMA     ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  Iphone11 Pro        64 GB     Rp. 15.800.000  ==  A5  ||")
                self.nama_hp = "Iphone 11 Pro"
                self.kapasitas = "64 GB"
                self.harga = 15800000
                self.tes = True
                self.loop = False
            elif self.kode == 'A6' or self.kode =='a6' :
                print("||  NAMA     ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  Iphone11 Pro Max    64 GB     Rp. 18.700.000  ==  A6  ||")
                self.nama_hp = "Iphone 11 Pro Max"
                self.kapasitas = "64 GB"
                self.harga = 18700000
                self.tes = True
                self.loop = False
            elif self.kode == 'A7' or self.kode =='a7' :
                print("||  NAMA     ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  Iphone12            64 GB     Rp. 14.999.000  ==  A7  ||")
                self.nama_hp = "Iphone 12"
                self.kapasitas = "64 GB"
                self.harga = 14999000
                self.tes = True
                self.loop = False
            elif self.kode == 'A8' or self.kode =='a8' :
                print("||  NAMA     ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  Iphone12 Mini       64 GB     Rp. 12.999.000  ==  A8  ||")
                self.nama_hp = "Iphone 12 Mini"
                self.kapasitas = "64 GB"
                self.harga = 12999000
                self.tes = True
                self.loop = False
            elif self.kode == 'A9' or self.kode =='a9' :
                print("||  NAMA     ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  Iphone12 Pro       128 GB     Rp. 18.499.000  ==  A9  ||")
                self.nama_hp = "Iphone 12 Pro"
                self.kapasitas = "128 GB"
                self.harga = 18499000 
                self.tes = True
                self.loop = False
            elif self.kode == 'A10' or self.kode =='a10' :
                print("||  NAMA     ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  Iphone12 Pro Max   128 GB     Rp. 20.499.000  ==  A10 ||")
                self.nama_hp = "Iphone 12 Pro Max"
                self.kapasitas = "128 GB"
                self.harga = 20499000 
                self.tes = True
                self.loop = False
                
        #samsung_Type
        
            elif self.kode == 'B1' or self.kode =='b1' :
                print("||  NAMA             ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  GalaxyS10 Silver           128 GB     Rp. 8.200.000   ==  B1  ||")
                self.nama_hp = "GalaxyS10 Silver"
                self.kapasitas = "128 GB"
                self.harga = 8200000
                self.tes = True
                self.loop = False
            elif self.kode == 'B2' or self.kode =='b2' :
                print("||  NAMA             ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  GalaxyS10 Gold             512 GB     Rp. 9.700.000   ==  B2  ||")
                self.nama_hp = "GalaxyS10 Gold "
                self.kapasitas = "512 GB"
                self.harga = 9700000 
                self.tes = True
                self.loop = False
            elif self.kode == 'B3' or self.kode =='b3' :
                print("||  NAMA             ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  GalaxyS10+ Silver          128 GB     Rp. 10.100.000  ==  B3  ||")
                self.nama_hp = "GalaxyS10+ Silver"
                self.kapasitas = "128 GB"
                self.harga = 10100000 
                self.tes = True
                self.loop = False
            elif self.kode == 'B4' or self.kode =='b4' :
                print("||  NAMA             ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  GalaxyS10+ Gold              1 TB     Rp. 15.500.000  ==  B4  ||")
                self.nama_hp = "GalaxyS10+ Gold"
                self.kapasitas = "1 TB"
                self.harga = 15500000  
                self.tes = True
                self.loop = False
            elif self.kode == 'B5' or self.kode =='b5' :
                print("||  NAMA             ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  GalaxyS10e                 128 GB     Rp. 10.297.000  ==  B5  ||")
                self.nama_hp = "GalaxyS10e"
                self.kapasitas = "128 GB"
                self.harga = 10297000 
                self.tes = True
                self.loop = False
            elif self.kode == 'B6' or self.kode =='b6' :
                print("||  NAMA             ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  GalaxyS20 FE               128 GB     Rp. 9.999.000   ==  B6  ||")
                self.nama_hp = "GalaxyS20 FE"
                self.kapasitas = "128 GB"
                self.harga = 9999000 
                self.tes = True
                self.loop = False
            elif self.kode == 'B7' or self.kode =='b7' :
                print("||  NAMA             ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  GalaxyS20                  128 GB     Rp. 14.499.000  ==  B7  ||")
                self.nama_hp = "GalaxyS20"
                self.kapasitas = "128 GB"
                self.harga = 14499000  
                self.tes = True
                self.loop = False
            elif self.kode == 'B8' or self.kode =='b8' :
                print("||  NAMA             ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  GalaxyS20+                 128 GB     Rp. 16.999.000  ==  B8  ||")
                self.nama_hp = "GalaxyS20+"
                self.kapasitas = "128 GB"
                self.harga = 16999000 
                self.tes = True
                self.loop = False
            elif self.kode == 'B9' or self.kode =='b9' :
                print("||  NAMA             ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  GalaxyS20 ULTRA            128 GB     Rp. 20.999.000  ==  B9  ||")
                self.nama_hp = "GalaxyS20 ULTRA"
                self.kapasitas = "128 GB"
                self.harga = 20999000
                self.tes = True
                self.loop = False
            elif self.kode == 'B10' or self.kode =='b10' :
                print("||  NAMA             ++++    Kapasitas ++    Harga        == KODE ||")
                print("||  GalaxyS20+ BTS Edition     128 GB     Rp. 17.499.000  ==  B10 ||")
                self.nama_hp = "GalaxyS20+ BTS Edition"
                self.kapasitas = "128 GB"
                self.harga = 17499000
                self.tes = True
                self.loop = False
            else :
                self.tes = False
                self.loop = True
                pass
                break  
    def Fix(self):
        while self.loop == True :
            print(" > Maaf Input yang anda inginkan tidak terdaftar !")
            print(" -. System Error !")
            print(" -. Input Salah / Tidak Sesuai !")
            self.Error = input("Apakah Ingin Kembali Ke Proses Sebelumnya ? (Y/N) : ")
            if self.Error == 'N' or self.Error =='n':
                print("=====================================================")
                print("============TERIMA KASIH ATAS KUNJUNGANNYA===========")
                print("============    SILAHKAN DATANG LAGI      ===========")
                print("=====================================================")
                self.tanya = input("Program Akan Kembali Ke Bagian Pemasukan Kode ? \n Masukkan (Y) untuk melanjutkan   : ")
                if self.tanya == 'Y' or 'y' :
                    print("||============================||||==================================||")
                    print("||    NAMA            == KODE ||||     NAMA                 == KODE ||")
                    print("||============================||||==================================||")
                    print("||  IphoneX           ==  A1  ||||  GalaxyS10 Silver        ==  B1  ||")
                    print("||  IphoneXs          ==  A2  ||||  GalaxyS10 Gold          ==  B2  ||")
                    print("||  IphoneXs MAX      ==  A3  ||||  GalaxyS10+ Silver       ==  B3  ||")
                    print("||  Iphone11          ==  A4  ||||  GalaxyS10+ Gold         ==  B4  ||")
                    print("||  Iphone11 Pro      ==  A5  ||||  GalaxyS10e              ==  B5  ||")
                    print("||  Iphone11 Pro Max  ==  A6  ||||  GalaxyS20 FE            ==  B6  ||")
                    print("||  Iphone12          ==  A7  ||||  GalaxyS20               ==  B7  ||")
                    print("||  Iphone12 Mini     ==  A8  ||||  GalaxyS20+              ==  B8  ||")
                    print("||  Iphone12 Pro      ==  A9  ||||  GalaxyS20 ULTRA         ==  B9  ||")
                    print("||  Iphone12 Pro Max  ==  A10 ||||  GalaxyS20+ BTS Edition  ==  B10 ||")
                    print("||============================||||==================================||")
                    self.kode = input("Masukkan Kode HP : ")
                    beli.sortir(self)
                    break
            elif self.Error == 'Y' or self.Error == 'y':
                self.kode = input("Masukkan Kode HP : ")
                beli.sortir(self)
                break
            else :
                beli.Fix(self)
                break
            
    def tampilan(self):
        if self.tes == True :
            print("\nBerikut adalah Hasil Pencarian Anda :")
            print(f'Kode        : {self.kode}\nNama HP     : {self.nama_hp}\nKapasitas   : {self.kapasitas}\nHarga       : Rp. {self.harga}')
        else :
            beli.Fix(self)
            
    def jumlah_beli(self):
        if self.tes == True :
            self.jumlah = int(input("Silahkan Masukkan Jumlah Barang Yang ingin dibeli : "))
            if self.tes == True and self.jumlah > 0 :
                self.sub_total = self.jumlah * self.harga
                if self.sub_total >= 17000000:
                    print("\n===================================")
                    print("Selamat Anda Mendapatkan Diskon 25%")
                    print("===================================")
                    self.diskon = "Diskon 25%"
                    self.total = self.sub_total- (self.sub_total * 0.25)
                elif self.sub_total >= 14000000 :
                    print("\n===================================")
                    print("Selamat Anda Mendapatkan Diskon 20%")
                    print("===================================")
                    self.diskon = "Diskon 20%"
                    self.total = self.sub_total- (self.sub_total * 0.20)
                elif self.sub_total >= 10000000 :
                    print("\n===================================")
                    print("Selamat Anda Mendapatkan Diskon 10%")
                    print("===================================")
                    self.diskon = "Diskon 10%"
                    self.total = self.sub_total- (self.sub_total * 0.10)
                elif self.sub_total >= 8000000 :
                    print("\n===================================")
                    print("Selamat Anda Mendapatkan Diskon 5%")
                    print("===================================")
                    self.diskon = "Diskon 5%"    
                    self.total = self.sub_total- (self.sub_total * 0.05)
                else :
                    print("\n !! Anda tidak mendapatkan Diskon !!")
                    self.total = self.sub_total
            else :
                print("> Terjadi Error Input Barang Yang Ingin di Beli ! ")
                print("> Harap Masukkan Jumlah yang Benar !")
                beli.jumlah_beli(self)
        else :
            beli.Fix(self)
            
    def pembelian(self):
        self.uang = int(input("Masukkan Jumlah Uang Anda : Rp. "))
        while self.tes == True :
            if self.uang >= self.total : 
                self.kembalian = float(self.uang - self.total) 
                self.cek = True
                self.tes = False
                break
            else :
                print(" \n!!Maaf Terjadi Error !!\n -. Jumlah Uang Anda Tidak Mencukupi\n -. Input Error\n -. System Error")
                self.cek = False
                self.tes = True
                beli.pembelian(self)
                break

    def tampilan_2(self):
        if self.cek == True :
                print("\n=====================================================")
                self.pelanggan.Person_info()
                print("============= P E M B E L I A N =====================")
                print(f"||Jenis HP                     : {self.nama_hp}")
                print(f"||Kapasitas                    : {self.kapasitas}")
                print(f"||Harga                        : {self.harga}")
                print(f"||Jumlah Pembelian             : {self.jumlah}")
                print("=====================================================")
                print(f'||Total bayar (Sebelum Diskon) : Rp. {self.sub_total}')
                print(f'||Diskon Yang Anda dapat       : {self.diskon}')
                print(f'||Jumlah Uang Anda             : Rp. {self.uang}')
                print("-----------------------------------------------------")
                print(f'||Total Pembayaran             : Rp. {self.total}')
                print(f'||Total Kembalian              : Rp. {self.kembalian}')
                print("=====================================================")
                print("============TERIMA KASIH ATAS PEMBELIANNYA===========")
                print("============    SILAHKAN DATANG LAGI      ===========")
                print("=====================================================") 
        else :
            pass
    

                         
if __name__ == "__main__":
    print ("|---------------------------------------------------------------|")
    print ("=====   *****       SELAMAT DATANG DI DINO CELL      *****  =====")
    print ("=================================================================")
    print ("|                        DISKON AKHIR TAHUN                     |")
    print ("|              TERMURAH , TERLENGKAP (Iphone , Samsung)         |")
    print ("|---------------------------------------------------------------|")
    print ("\n== Personal Info ==")
    Nama = input("Nama Anda     : ")
    NoHp = int(input("Nomor Hp Anda : "))
    Umur = int(input("Umur Anda     : "))
    
def main() :
        i = True
        while i == True : 
            Pilihan = int(input("Berikut adalah List Merek \n 1. Iphone \n 2. Samsung \n Silahkan Masukkan Pilihan Anda (1 atau 2) ? : "))
            user = Cells(Nama,Umur,NoHp, Pilihan)
            if Pilihan == 1 :
                user.tampilan()
                i = False
            elif Pilihan == 2 :
                user.tampilan()
                i = False
            else :
                i = True 
                main()
                break
        Kode = input("Masukkan Kode HP : ")
        print("\n")
        user2 = beli(user,Kode)
        def coba_lagi():
            while True :
                print(" > Data Accepted..")
                coba = input("Apakah Ingin Mengulangi Proses Pembelian atau Membuat pembelian baru ? (Y/N) : ")
                if coba == 'Y' or coba =='y':
                    main()
                elif coba == 'N' or coba == 'n':
                    user2.tampilan_2()
                    break
                else :
                    coba_lagi()
                    break     
        user2.sortir()
        user2.Fix()
        user2.tampilan()
        user2.jumlah_beli()
        user2.pembelian()
        coba_lagi() 
main()
