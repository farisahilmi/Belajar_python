class Kampus:
    nama = ""
    alamat = ""

class Mahasiswa:
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"halo nama saya {self.nama}")

kampus1 = Kampus()
kampus2 = Kampus()

print(type(kampus1))
print(type(kampus2))

mahasiswa1 = Mahasiswa()
mahasiswa1.nim = 12345
mahasiswa1.nama = "faris"

print(mahasiswa1.nim)
print(mahasiswa1.nama)

mahasiswa2 = Mahasiswa()
mahasiswa2.nim = 33445
mahasiswa2.nama = "aceng"

print(mahasiswa2.nim)
print(mahasiswa2.nama)

print(type(mahasiswa1))
print(type(mahasiswa2))