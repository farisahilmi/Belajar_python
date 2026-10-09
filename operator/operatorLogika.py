#operator logika
# operator logika digunakan untuk menggabungkan atau memodifikasi nilai boolean
# and (dan), menghasilkan True jika kedua kondisi True
# or (atau), menghasilkan True jika salah satu kondisi True
# not (tidak), membalik nilai boolean

umur = 25
print(umur > 18 and umur < 30) # True (25 > 18 dan 25 < 30)

hari = "sabtu"
print(hari == "sabtu" or hari == "minggu") # True

aktif = True
print(not aktif) # False