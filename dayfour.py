hari = "selasa"
kegiatan = "sekolah"
berangkat = int(input("Jam berangkat: "))
if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis" or hari == "jumat":
    if kegiatan == "sekolah":
        if berangkat < 6:
            print("Berangkat terlalu pagi, sebaiknya tidur lagi.")
        elif berangkat >= 6 and berangkat <= 7:
            print("Berangkat tepat waktu untuk sekolah.")
        else:
            print("Terlambat berangkat ke sekolah.")
    else:
        print("Hari ini tidak ada kegiatan sekolah.")

if hari == "sabtu" or hari == "minggu":
    print("Hari ini libur, tidak ada kegiatan sekolah.")
    if kegiatan == "sekolah":
        print("Tapi kegiatan sekolah tetap ada, sebaiknya tetap berangkat.")
    print("Selamat menikmati libur akhir pekan!")
    