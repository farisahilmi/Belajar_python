firstName = "farisa"
lastName = "Hilmi"

newname = "    Rido cliptria "

fullName = firstName + " " + lastName

print(fullName.upper()) # Huruf nya jadi besar semuanya
print(fullName.lower()) # huruf nya jadi kecil semuanya
print(fullName.title()) # Huruf pertama di setiap kata jadi besar
print(fullName.capitalize()) # huruf pertama awal karakter jadi huruf besar
print(newname.strip()) # menghapus spasi di awal dan akhir
print(fullName.replace("farisa", "denis")) # mengganti (dari, menjadi) untuk mengganti bagian tertentu dalam string
print(fullName.count("farisa")) # untuk menghitung jumlah kata tertentu dalam string
print(fullName.find("farisa")) # untuk mencari kata tertentu dalam string, jika tidak ada akan mengembalikan -1