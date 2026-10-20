# mencari huruf dalam kata
kata = input("masukkan kata: ")
huruf_dicari = input("masukkan huruf yang dicari: ")

for huruf in kata:
    if huruf == huruf_dicari:
        print("Huruf", huruf_dicari, "ditemukan dalam kata!")
        break
else:
    print("Huruf", huruf_dicari, "tidak ditemukan dalam kata")
