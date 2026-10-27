try:
    angka = int(input("Masukkan angka: "))
    print("Angka Anda:", angka)
except ValueError:
    print("input tidak valid!")
finally:
    print("program selesai dijalankan error atau tidak pun")