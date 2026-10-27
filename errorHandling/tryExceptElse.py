try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input tidak valid!")
else:
    print("Angka yang anda masukkan:", angka)
    if angka > 0:
        print("angka positif")
    elif angka < 0:
        print("angka negatif")
    else:
        print("angka nol")