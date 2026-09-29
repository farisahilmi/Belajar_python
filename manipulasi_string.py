nama = "budi"
umur = 25

# cara yang salah (akan error)
# pesan = "Nama saya" + nama + ", umur" + umur

# cara yang benar
pesan = "Nama saya " + nama + ", umur " + str(umur) 

print(pesan)

print(len(nama))
print(len(pesan))

# Indexing
name = "Python"
print(name[0]) # P (Karakter pertama)
print(name[1]) # y (karakter kedua)
print(name[2]) # t (karakter ketiga)

print(name[-1]) # n (karakter terakhir)
print(name[-2]) # o (karakter kedua dari belakang)
print(name[-3]) # h (karakter ketiga dari belakang)


# String Slicing
name = "python"
print(name[0:3]) # pty (index 0, 1, 2)
print(name[2:5]) # tho (index 2, 3, 4)
print(name[1:4]) # yth (index 1, 2, 3)

name = "python"
print(name[:3]) # pyt (dari awal sampai index 2)
print(name[2:]) # thon (dari index 2 sampai akhir)
print(name[:]) # python (seluruh string)