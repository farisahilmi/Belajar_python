# mencetak angka 1 sampai 5
angka = 1
while angka <= 5:
    print(angka)
    angka += 1

# input sampai benar
password = ""
while password != "123456":
    password = input("masukkan password: ")
    if password != "123456":
        print("password salah, coba lagi!")


print("Password benar!")