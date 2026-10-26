point = (5, 10)
print(point[0])     # 5
print(point[1])     # 10

# untuk data yang tidak berubah 
tanggal_lahir = (15, 8, 1990)   # tanggal, bulan, tahun
print("tanggal lahir: ", tanggal_lahir) # dengan tanda kurung
print("tanggal lahir: ", *tanggal_lahir) # unpacking (tanpa tanda kurung)

# iterasi di tuple
for e in tanggal_lahir:
    print(e)

# iterasi di tuple dengan index
for i in range(len(tanggal_lahir)):
    print(tanggal_lahir[i])