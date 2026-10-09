# kita bisa menempatkan if di dalam if yang lain 

username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "123456":
        print("Login berhasil")
        print("Selamat datang admin")
    else:
        print("password salah")
else: 
    print("username tidak ditemukan")