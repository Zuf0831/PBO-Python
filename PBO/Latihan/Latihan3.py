class operasi :
    def __init__(self):
        self.A = 10
        self.B = 5
    def cetak(self):
        print(f'A = {self.A}')
        print(f'B = {self.B}')
        
class penjumlahan(operasi):
    def cetak(self):
        print(f'Penjumlahan : {self.A+self.B}')

class pengurangan(operasi):
    def cetak(self):
        print(f'Pengurangan : {self.A-self.B}')

class perkalian(operasi):
    def cetak(self):
        print(f'Perkalian   : {self.A*self.B}')
    
class pembagian(operasi):
    def cetak(self):
        print(f'Pembagian   : {self.A/self.B}')
        
showup = operasi()
showup.cetak()
x = penjumlahan()
x.cetak()
y = pengurangan()
y.cetak()
z = perkalian()
z.cetak()
xx = pembagian()
xx.cetak()