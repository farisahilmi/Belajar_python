# main.py

from membuatModuleSendiri import matematika

if __name__ == "__main__":
# Gunakan function dari module
    hasil1 = matematika.tambah(10, 5)
    hasil2 = matematika.kali(7, 3)

    print("10 + 5 =", hasil1)
    print("7 x 3 =", hasil2)

    # Gunakan variables dari module
    print("Nilai PI:", matematika.PI)
    print("Dibuat oleh:", matematika.NAMA_PEMBUAT)