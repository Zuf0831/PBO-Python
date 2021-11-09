'''
Nama : Yusuf Sulle
Kelas : TK-43-01
Nim : 1103194015
'''

#Tugas 3

nama = input("Nama Pegawai          : ")
nip = int(input("NIP Pegawai           : "))
status = input("Status Pegawai        : ")
gol = input("Golongan              : ")

if status == "programmer" :
    gajipok = 12000000
    if gol == "junior":
        bonus = 500000
        gaji = gajipok + bonus 
    elif gol == "senior":
        bonus = 1000000
        gaji = gajipok + bonus 

if status == "ui" :
    gajipok = 10000000
    if gol == "junior":
        bonus = 400000
        gaji = gajipok + bonus 
    elif gol == "senior":
        bonus = 900000
        gaji = gajipok + bonus 

if status == "ux" :
    gajipok = 9500000
    if gol == "junior":
        bonus = 600000
        gaji = gajipok + bonus 
    elif gol == "senior":
        bonus = 300000
        gaji = gajipok + bonus 

if status == "analyst" :
    gajipok = 10500000
    if gol == "junior":
        bonus = 300000
        gaji = gajipok + bonus 
    elif gol == "senior":
        bonus = 600000
        gaji = gajipok + bonus 


print ("\nTotal Gaji            : ",gaji)