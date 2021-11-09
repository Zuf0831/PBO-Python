class tanah:
    def __init__(self):
        self.panjang = 100
        self.lebar = 200
        
class luas(tanah):
    def __init__(self):
        super().__init__()
    
    def get_Luas(self):
        self.Luas = int((self.panjang*self.lebar)/2)
        self.harga = self.Luas * 350000
        print(f'Luas Tanah   : {self.Luas} Meter')
        print(f'Harga Tanah  : RP.{self.harga}')

x = luas()
x.get_Luas()