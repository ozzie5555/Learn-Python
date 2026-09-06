name = "John"
kelas = "XII SIJA 1"

if __name__ == "__main__":
    print("Nama:", name)
    print("Kelas:", kelas)

if __name__ == "__main__":
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
else:
    print("Program ini tidak dijalankan secara langsung.")
    if __name__ == "__main__":
        hari = "sabtu"
        kegiatan = "libur"
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
            
        if __name__ == "__main__":
                hari = "minggu"
                kegiatan = "libur"
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