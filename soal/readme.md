# Latihan Python - Soal 1 sampai 5 🐍

Repository ini berisi latihan Python dengan **kode yang sengaja salah**.
Tugas: temukan kesalahannya dan perbaiki!

## 🎯 Aturan Latihan

1. Jangan langsung lihat kunci jawaban
2. Jalankan kode dulu, baca error-nya
3. Perbaiki satu per satu
4. Commit setiap soal yang sudah selesai

## 🚀 Cara Menjalankan

```bash
cd soal
python p1.py
python p2.py
python p3.py
python p4.py
python p5.py
```

---

## Soal 1: Nilai Rata-rata Siswa

**File:** `soal/p1.py`

Program menghitung rata-rata nilai dan menentukan status kelulusan.

**Target Output:**
```
Nama siswa: Andi
Nilai rata-rata: 82.5
Status: LULUS
Predikat: B
```

**Hint:** Ada kesalahan di bagian `if`. Cek penggunaan `:` dan `=`.

---

## Soal 2: Program Belanja Sederhana

**File:** `soal/p2.py`

Program kasir menghitung total belanja dan diskon.

**Target Output:**
```
Buku x 2 = 30000
Pulpen x 5 = 25000
Penghapus x 3 = 9000
Total bayar: Rp 64000
Diskon: Rp 6400.0
Total akhir: Rp 57600.0
```

**Hint:** Cek logika `if` diskon. Pastikan perhitungannya benar.

---

## Soal 3: Cek Bilangan Prima

**File:** `soal/p3.py`

Program mengecek apakah suatu bilangan prima atau bukan.

**Target Output:**
```
2 adalah bilangan prima
3 adalah bilangan prima
4 bukan bilangan prima
5 adalah bilangan prima
7 adalah bilangan prima
9 bukan bilangan prima
11 adalah bilangan prima
15 bukan bilangan prima
```

**Hint:** Logika `return` di dalam function terbalik. Bilangan prima hanya bisa dibagi 1 dan dirinya sendiri.

---

## Soal 4: Program Login Sederhana

**File:** `soal/p4.py`

Program login dengan maksimal 3 percobaan.

**Target Output (jika login berhasil):**
```
Percobaan ke- 1
Masukkan username: admin
Masukkan password: 12345
Selamat datang, admin
```

**Target Output (jika 3x gagal):**
```
Percobaan ke- 1
...
Akun terkunci. Coba lagi nanti.
```

**Hint:** Cek penggunaan `=` vs `==` di bagian pengecekan `login_berhasil`.

---

## Soal 5: Data Mahasiswa

**File:** `soal/p5.py`

Program menyimpan dan menampilkan data mahasiswa, cari nilai tertinggi, dan rata-rata.

**Target Output:**
```
Mahasiswa terbaik: Dewi
Nilainya: 95
Rata-rata kelas: 86.25
Mahasiswa di atas rata-rata:
- Siti : 90
- Dewi : 95
```

**Hint:** Perhatikan operator pembagian `//` vs `/`. Untuk hasil desimal, gunakan `/`.

---