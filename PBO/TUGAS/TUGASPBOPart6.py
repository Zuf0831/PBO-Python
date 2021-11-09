def deret(n_awal,n_akhir,jarak):
    if n_awal <= n_akhir :
        print (n_awal, end=" ")
    if n_awal <= n_akhir :
        deret(n_awal+jarak,n_akhir,jarak)
    else :
        print(" ")
deret (1,10,1)
deret (1,10,2)
deret (10,30,5)