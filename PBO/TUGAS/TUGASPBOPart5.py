def pangkat (x,y) :
    if y == 0 :
        return 1
    else : 
        return x*pangkat(x,y-1)

x = int(input("Masukkan x : "))
y = int(input("Masukkan y : "))
print (f'hasil = {pangkat(x,y)}')

