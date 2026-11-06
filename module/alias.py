# main.py

from membuatModuleSendiri.matematika import matematika as math

if __name__ == "__main__":
# Gunakan function dari module
    hasil1 = math.tambah(10, 5)
    hasil2 = math.kali(7, 3)

    print("10 + 5 =", hasil1)
    print("7 x 3 =", hasil2)

    # Gunakan variables dari module
    print("Nilai PI:", math.PI)
    print("Dibuat oleh:", math.NAMA_PEMBUAT)