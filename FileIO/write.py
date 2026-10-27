print("=== SIMPAN DATA NILAI ===")

file = open("nilai_siswa.txt", "w")

while True:
    nama = input("Nama siswa (enter untuk selesai): ")
    if nama == "":
        break

    nilai = input("nilai: ")

    # tulis ke file
    file.write(nama + "," + nilai + "\n")
    print("data", nama, "berhasil disimpan")

file.close()
print("semua data berhasil disimpan ke nilai_siswa.txt")