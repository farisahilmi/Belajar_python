# mencetak angka ganjil saja
for i in range(10):
    if i % 2 == 0:  # jika genap
        continue    # lewati, lanjut ke angka berikutnya
    print(i)        # hanya mencetak angka ganjil
