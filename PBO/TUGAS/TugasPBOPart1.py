year_list = [] 

n = int(input("Masukkan Jumlah Data : ")) 

print ("Perhatian!! Input pertama merupakan Tahun Kelahiran Anda !!")
for i in range(0, n): 
    tahun = int(input()) 
    year_list.append(tahun)    
print("List Tahun = " , year_list) 

umur = year_list[0]
print ("Umur kamu sekarang adalah :" ,umur)
print ("Umur pada 2 Tahun kedepan " , int(umur+2))
print ("Umur paling tua didalam List :" , max(year_list))

