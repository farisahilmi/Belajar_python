# mengakses elemen 
buah = ["apel", "jeruk", "pisang", "mangga"]
print(buah[0])  # apel
print(buah[1])  # jeruk
print(buah[2])  # pisang
print(buah[3])  # mangga
print(buah[-1]) # mangga (elemen terakhir)

# mengubah elemen 
warna = ["merah", "biru", "hijau"]
print(warna)    # ['merah', 'biru', 'hijau']
warna[1] = "kuning"
print(warna)    # ['merah', 'kuning', 'hijau']

# append() - menambah di akhir
buah = ["apel", "jeruk"]
buah.append("pisang")
print(buah)     # ["apel", "jeruk", "pisang"]

angka = [1, 2, 3, 4, 5]
# remove - menghapus nilai tertentu
angka.remove(3)
print(angka)    # [1, 2, 4, 5]

# pop() - menghapus elemen terakhir
angka.pop()
print(angka)    # [1, 2, 4]

# del - menghapus berdasarkan index
del angka[0]
print(angka)    # [2, 4]

# panjang list
buah = ["apel", "jeruk", "pisang"]
print(len(buah))    # 3

# menggabungkan list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
gabungan = list1 + list2
print(gabungan) # [1, 2, 3, 4, 5, 6]

# mengecek apakah elemen ada dalam list
if "apel" in buah:
    print("apel tersedia")

buah = ["apel", "jeruk", "pisang"]

# menggunakan for loop 
print("Daftar buah: ")
for item in buah:
    print("-", item)

# dengan index
for i in range(len(buah)):
    print(str(i+1) + ".", buah[i])