while True: 
    print("=== KALKULATOR SEDERHANA ===")
    print("1. tambah")
    print("2. kurang")
    print("3. kali")
    print("4. bagi")
    print("5. keluar")

    try:
        operator = int(input("Masukkan Operator (contoh : 1-5): "))

        if operator == 5:
            print("terima kasih sudah menggunakan kalkulator ini")
            break

        if operator not in [1, 2, 3, 4]:
            print("operator tidak valid. pilih angka 1-5.")
            continue

        angka1 = int(input("Masukkan Angka Pertama: "))
        angka2 = int(input("Masukkan Angka Kedua: "))

        if operator == 1:
            hasil = angka1 + angka2
            print("hasil tambah: ", hasil)
        elif operator == 2:
            hasil = angka1 - angka2
            print("hasil kurang:", hasil)
        elif operator == 3:
            hasil = angka1 * angka2
            print("hasil kali:", hasil)
        elif operator == 4:
            hasil = angka1 / angka2
            print("hasil bagi: ", hasil)
    except ValueError:
        print("input harus berupa angka!")
    except ZeroDivisionError:
        print("Tidak bisa dibagi dengan Nol!")
    else: 
        print("perhitungan selesai")
    finally:
        print("=== Kalkulator sudah selesai ===")