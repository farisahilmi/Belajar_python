def perkenalan(nama, umur, kota):
    print("nama:", nama)
    print("umur:", umur, "tahun")
    print("asal:", kota)
    print("---")


# Positional arguments (urutan harus sesuai)
perkenalan("alice", 25, "jakarta")

# Keyword arguments (urutan bebas)
perkenalan(kota="Bandung", nama="Bob", umur=30)
perkenalan(umur=28, kota="Surabaya", nama="Charlie")


def buat_profil(nama, umur, kota="jakarta", pekerjaan="Belum bekerja"):
    print(f"=== Profil {nama.upper()} ===")
    print(f"umur: {umur} tahun")
    print(f"kota: {kota}")
    print(f"pekerjaan: {pekerjaan}")
    print()

# Positional + keyword arguments
buat_profil("Alice", 25)    # Menggunakan default
buat_profil("Bob", 30, kota="Bandung")
buat_profil("Charlie", 28, pekerjaan="Developer")
buat_profil("Diana", kota="Surabaya", umur=35, pekerjaan="Designer")