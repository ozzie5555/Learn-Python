# Program menyimpan dan menampilkan data mahasiswa

mahasiswa = [
    {"nama": "Budi", "nim": "001", "nilai": 85},
    {"nama": "Siti", "nim": "002", "nilai": 90},
    {"nama": "Rudi", "nim": "003", "nilai": 75},
    {"nama": "Dewi", "nim": "004", "nilai": 95}
]

# Cari nilai tertinggi
nilai_tertinggi = 0
mahasiswa_terbaik = ""

for mhs in mahasiswa:
    if mhs["nilai"] > nilai_tertinggi:
        nilai_tertinggi = mhs["nilai"]
        mahasiswa_terbaik = mhs["nama"]

print("Mahasiswa terbaik:", mahasiswa_terbaik)
print("Nilainya:", nilai_tertinggi)

# Hitung rata-rata
total = 0
for mhs in mahasiswa:
    total = total + mhs["nilai"]

rata = total // len(mahasiswa)
print("Rata-rata kelas:", rata)

# Tampilkan semua mahasiswa yang nilainya di atas rata-rata
print("Mahasiswa di atas rata-rata:")
for mhs in mahasiswa:
    if mhs["nilai"] > rata:
        print("-", mhs["nama"], ":", mhs["nilai"])