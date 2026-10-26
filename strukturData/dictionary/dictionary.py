# Dictionary dengan data

siswa = {
    "nama": "Alice",
    "umur": 20,
    "kelas": "12A"
}

print(siswa)

print(siswa["nama"])    # Alice
print(siswa["umur"])    # 20
print(siswa["kelas"])   # 12A

print(*siswa.items(), sep="\n")
# Mengubah nilai 
siswa["umur"] = 21
print(siswa)

# Menghapus key-value
del siswa["kelas"]
print(siswa)

# Mengiterasi keys
for key in siswa:
    print(key, ":", siswa[key])

# Mengiterasi key-value pairs
for key, value in siswa.items():
    print(key, "=", value)