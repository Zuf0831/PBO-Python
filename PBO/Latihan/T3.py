file = open('T3.txt', 'w')


class barang:

     jumlah_alatTulis = 0
     jumlah_harga_100 = 0
     harga = []
     barang_10k = []

     def init(self, nama, jenis, stok, harga_satuan):
         self.nama = nama
         self.jenis = jenis
         self.stok = stok
         self.harga_satuan = harga_satuan
         if(self.jenis == "Alat Tulis"):
             barang.jumlah_alatTulis += 1
         barang.harga.append(self.harga_satuan)
         if(self.harga_satuan > 10000):
             barang.barang_10k.append(self.nama)

     def nulis_file(self):
         file.write(self.nama)
         file.write(" ")
         file.write(self.jenis)
         file.write(" ")
         file.write(str(self.stok))
         file.write(" ")
         file.write(str(self.harga_satuan))
         file.write("\n")