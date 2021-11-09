buah = ["nangka","durian","mangga"]

for x in buah :
    print (x.upper(),end=" ")
print(" ")
buah.append("apel")
for x in buah :
    print (x.upper(),end=" ")
del buah[2]
print(" ")
print(buah)