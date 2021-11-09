'''
Nama    :   YUSUF SULLE
KELAS   :   TK-43-01
NIM     :   1103194015
'''
baris = int(input("Masukkan jumlah baris : "))
colom = int(input("Masukkan jumlah kolom : "))

M = []

for i in range (baris):
    T= []
    for j in range(colom):
        T.append(int(input()))
    M.append(T)
    

print("Matriks Asli : ")
for i in range(baris):
    for j in range(colom):
        print(M[i][j], end = " ")
    print()

print("Matriks transpose : ")
for i in range(baris):
    for j in range(colom):
        print(M[j][i], end = " ")
    print()
