# Program menghitung nilai rata-rata dan status kelulusan

nama_siswa = "Andi"
nilai = [80, 75, 90, 85]

total = 0
for n in nilai:
    total = total + n

rata_rata = total / len(nilai)
print("Nama siswa:", nama_siswa)
print("Nilai rata-rata:", rata_rata)

if rata_rata > 80
    print("Status: LULUS")
else:
    print("Status: TIDAK LULUS")

if rata_rata >= 90:
    print("Predikat: A")
elif rata_rata >= 80:
    print("Predikat: B")
elif rata_rata >= 70:
    print("Predikat: C")