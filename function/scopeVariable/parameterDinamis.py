def cetak_list(*list):
    for item in list:
        print(item)

cetak_list(1, 2, 3, 4, 5)


def cetak_dict(**dict):
    for key, value in dict.items():
        print(f"{key}: {value}")


cetak_dict(nama="Alice", umur=25, kota="jakarta")