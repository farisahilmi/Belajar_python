# conditional expression memungkinkan kita menulis kondisi sederhana dalam satu baris

angka = int(input("masukkkan angkga: "))

# dengan if-else biasa
if angka > 0:
    hasil = "Positif"
else: 
    hasil = "Non-positif"


# dengan ternary operator (lebih singkat)
hasil = "Positif" if angka > 0 else "Non-positif"
print("Angka tersebut:", hasil)