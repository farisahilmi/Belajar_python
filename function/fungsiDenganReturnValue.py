def hitung_luas_lingkaran(radius):
    pi = 3.14159
    luas = pi * radius * radius
    return luas

luas1 = hitung_luas_lingkaran(5)
luas2 = hitung_luas_lingkaran(10)

print("luas lingkaran radius 5:", luas1)
print("luas lingkaran radius 10:", luas2)
print("total luas:", luas1 + luas2)