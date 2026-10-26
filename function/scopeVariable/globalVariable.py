nama_global = "Alice"   # Global variable

def tampilkan_nama():
    print("Nama:", nama_global)     # bisa mengakses global variable

def ubah_nama():
    global nama_global
    nama_global = "Bob" # Mengubah global variable

tampilkan_nama()    #   Alice
ubah_nama() 
tampilkan_nama()    #   Bob