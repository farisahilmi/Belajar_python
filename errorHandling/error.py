print("=== KALKULATOR SEDERHANA ===")

try:
    angka1 = int(input("Angka pertama: "))
    angka2 = int(input("Angka kedua: "))
    hasil = angka1 / angka2
    print("Hasil:", hasil)
except ValueError:
    print("Mohon masukkan angka yang valid!")
except ZeroDivisionError:
    print("Tidak bisa dibagi dengan nol!")
except:
    print("Terjadi kesalahan yang lain!")