'''
Nama : Yusuf Sulle
Kelas : TK-43-01
Nim : 1103194015
'''

#Tugas 2

nama = input("Nama      :   ")
umur = int(input("umur      :   "))

if umur <= 5 :
    kat = "Balita" 
elif umur > 5 and umur <=13:
    kat = "Anak-Anak"
elif umur > 13 and umur <=25:
    kat = "Remaja"
elif umur > 25 and umur <=35:
    kat = "Dewasa"
elif umur > 35 and umur <=55:
    kat = "Orang Tua"
elif umur > 55 :
    kat = "Lanjut Usia"
    
print ("Anda berada di kategori : ",kat)