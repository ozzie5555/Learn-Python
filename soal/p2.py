# Program kasir sederhana

daftar_barang = ["Buku", "Pulpen", "Penghapus"]
harga = [15000, 5000, 3000]
jumlah_beli = [2, 5, 3]

total_bayar = 0

for i in range(len(daftar_barang)):
    subtotal = harga[i] * jumlah_beli[i]
    total_bayar = total_bayar + subtotal
    print(daftar_barang[i], "x", jumlah_beli[i], "=", subtotal)

print("Total bayar: Rp", total_bayar)

# Diskon 10% jika total > 50000
if total_bayar > 50000:
    diskon = total_bayar * 10 / 100
    total_bayar = total_bayar - diskon
    print("Diskon: Rp", diskon)

print("Total akhir: Rp", total_bayar)