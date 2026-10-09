nama = "Alice"
umur = 25
kota = "Jakarta"

# Menggunakan f-string
profil = f"Halo, nama saya {nama}, umur {umur} tahun, tinggal di {kota}"
print(profil)

# lebih jelas dibandingkan concatenation
profil_lama = "Halo, nama saya " + nama + ", umur " + str(umur) + " tahun, tinggal di " + kota
print(profil_lama)

# f-strings dengan Expressions
# f-strings dapat mengeksekusi ekspresi langsung di dalamnya
harga = 100000
jumlah = 3

# Operasi matematika dalam f-string
total = f"Total: Rp {harga * jumlah:,}" #format specifier
print(total)