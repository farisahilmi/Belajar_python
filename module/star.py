# main.py

from membuatModuleSendiri.matematika import *

if __name__ == "__main__":
# Gunakan function dari module
    hasil1 = tambah(10, 5)
    hasil2 = kali(7, 3)

    print("10 + 5 =", hasil1)
    print("7 x 3 =", hasil2)

    # Gunakan variables dari module
    print("Nilai PI:", PI)
    print("Dibuat oleh:", NAMA_PEMBUAT)