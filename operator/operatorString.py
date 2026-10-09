# operator string
# operator khusus untuk bekerja dengan string.
# concatenation (+), menambah string
# repetition (*), mengulang string sejumlah angka
# membership (in), mengecek apakah text ada dalam string

nama_depan = "John"
nama_belakang = "doe"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap) # John doe

kata = "Hello"
print(kata * 3) # HelloHelloHello

print(" ".join([kata] * 3))

garis = "-"
print(garis * 20)  # -------------------

kalimat = "Python adalah bahasa pemrograman"
print("Python" in kalimat)  # True
print("Java" in kalimat)    # False
print("adalah" in kalimat)  # True