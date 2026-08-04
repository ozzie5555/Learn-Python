pembeli = input("Masukkan nama pembeli: ")
nama_barang = "tablet"
harga = 230000
penjual = input("Masukkan nama penjual: ")
print("Nama pembeli:", pembeli)
print("Nama barang:", nama_barang)
print("Harga barang:", harga) 

if penjual == "Toko A":
    print("Penjual:", penjual)
    print("Barang tersedia di Toko A.")
elif penjual == "Toko B":
    print("Penjual:", penjual)
    print("Barang tersedia di Toko B.") 

else:
    print("Penjual:", penjual)
    print("Maaf, barang tidak tersedia di toko tersebut.")

print("Terima kasih telah berbelanja di toko kami!")
