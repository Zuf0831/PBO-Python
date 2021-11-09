class Toko:

     total_harga = 0

     def __init__(self, nama, stok, harga_satuan):
         self.nama = nama
         self.stok = stok
         self.harga_satuan = harga_satuan
         Toko.total_harga += (self.stok*self.harga_satuan)

     def tampilkan(self):
         print("Nama : ", self.nama)
         print("Stok : ", self.stok)
         print("Harga Satuan : ", self.harga_satuan)
         print("Harga : ", self.harga_satuan*self.stok)
         print()

     def totalHarga(self):
         print("Total Harga : ", Toko.total_harga)


crayon = Toko("Crayon", 10, 20000)
pensil = Toko("Pensil", 5, 1000)
penghapus = Toko("Penghapus", 4, 500)

crayon.tampilkan()
pensil.tampilkan()
penghapus.tampilkan()

print("Total Harga : ", Toko.total_harga)




