# karena kondisi harus bernilai boolean, artinya kita bisa menggunakan operator, misal operator logika, seperti and, or dan not

umur = int(input("masukkan umur: "))
punya_sim = input("punya sim? (ya/tidak): ")

if umur >= 17 and punya_sim.strip().lower() == "ya":
    print("Boleh mengendarai motor")
else:
    print("Tidak boleh mengendarai motor")