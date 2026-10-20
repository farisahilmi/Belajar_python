# game tebak angka dengan break
angka_rahasia = 7

while True:
    tebakan = int(input("Tebak angka (1-10): "))

    if tebakan == angka_rahasia:
        print("selamat! anda benar!")
        break
    else:
        print("salah, coba lagi!")