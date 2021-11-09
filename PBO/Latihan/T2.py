class Mhs:
     jmlh_lls = 0
     jmlh_nilai = 0

     def __init__(self, nama, nim, kelas, ipk):
         self.nama = nama
         self.nim = nim
         self.kelas = kelas
         self.ipk = ipk

     def rata(self):
         Mhs.jmlh_nilai += self.ipk

     def lls(self):
         if(self.ipk > 2.75):
             Mhs.jmlh_lls += 1

     def tampil(self):
         print("Nama : ", self.nama)
         print("NIM  : ", self.nim)
         print("Kelas : ", self.kelas)
         print("IPK : ", self.ipk)
         print()


Mhs1 = Mhs("Yusuf", 1103194015, "TK-43-01", 3.9)
Mhs2 = Mhs("Rayhan", 110319423, "TK-43-01", 3.5 )
Mhs3 = Mhs("Adlan", 110329436, "TK-43-01", 3.2)
Mhs4 = Mhs("Bintang", 1103344117, "TK-43-01", 3.4)
Mhs5 = Mhs("Imada", 1103454118, "TK-43-01", 3.3)
Mhs6 = Mhs("Ipul", 1103194115, "TK-43-01", 2.6)
Mhs7 = Mhs("Nauval", 1132194120, "TK-43-01", 2.8)
Mhs8 = Mhs("Ariq", 1103123121, "TK-43-01", 3.6)
Mhs9 = Mhs("Iqbal", 1103123110, "TK-43-01", 3.2)
Mhs10 = Mhs("Agustio", 1112394113, "TK-43-01", 3.8)


Mhs1.tampil()
Mhs2.tampil()
Mhs3.tampil()
Mhs4.tampil()
Mhs5.tampil()
Mhs6.tampil()
Mhs7.tampil()
Mhs8.tampil()
Mhs9.tampil()
Mhs10.tampil()

Mhs1.rata()
Mhs2.rata()
Mhs3.rata()
Mhs4.rata()
Mhs5.rata()
Mhs6.rata()
Mhs7.rata()
Mhs8.rata()
Mhs9.rata()
Mhs10.rata()

Mhs1.lls()
Mhs2.lls()
Mhs3.lls()
Mhs4.lls()
Mhs5.lls()
Mhs6.lls()
Mhs7.lls()
Mhs8.lls()
Mhs9.lls()
Mhs10.lls()

print("Rata-Rata IPK : ", Mhs.jmlh_nilai/10)
print("Mahasiswa yang Lulus : ", Mhs.jmlh_lls)
