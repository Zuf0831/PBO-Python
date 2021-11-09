class JNE :
    def __init__(self, nama ,panjang,lebar,tinggi):
        self.nama = nama
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        
class pengiriman(JNE):
    def __init__(self, nama,panjang, lebar, tinggi, tujuan):
        super().__init__(nama,panjang, lebar, tinggi)
        self.tujuan = tujuan
    
    def tempat(self):
        self.volume = int((self.panjang * self.lebar * self.tinggi)/6000)
        if self.tujuan == "semarang":
            self.tarif = 20000
            self.waktu = "2 - 3 Hari"
            self.harga = int(self.volume * self.tarif)
        
        elif self.tujuan == "jakarta":
            self.tarif = 11000
            self.waktu = "3 - 4 Hari"
            self.harga = int(self.volume * self.tarif)
    
    def tampilan(self):
        print("== SELAMAT DATANG DI JASA PENGIRIMAN JNE ==")
        print(f'Nama Barang         : {self.nama}')
        print(f'Volume Barang       : {self.volume}')
        print(f'Tujuan              : {self.tujuan}')
        print(f'Tarif               : Rp.{self.tarif}/KG')
        print(f'Estimasi Waktu      : {self.waktu}')
        print(f'Total Harga         : Rp.{self.harga}')
        print("\n")
        
if __name__ == "__main__" :
    x = pengiriman("Helm", 40, 30, 10, "semarang")
    y = pengiriman("Lemari", 100, 70, 120, "jakarta")
    x.tempat()
    y.tempat()
    x.tampilan()
    y.tampilan()