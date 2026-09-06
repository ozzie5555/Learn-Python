waktu : 'malam'
jam : 22
lokasi : 'rumah'

if __name__ == "__main__":
    if waktu == 'malam' and jam >= 22 and lokasi == 'rumah':
        print("Waktunya tidur, selamat malam!")
    else:
        print("Masih ada waktu untuk beraktivitas.")
        if waktu == 'pagi' and jam < 12:
            print("Selamat pagi! Semoga harimu menyenangkan.")
        elif waktu == 'siang' and jam >= 12 and jam < 18:
            print("Selamat siang! Semoga harimu produktif.")
        elif waktu == 'sore' and jam >= 18 and jam < 22:
            print("Selamat sore! Semoga harimu menyenangkan.")
            if waktu == 'malam' and jam >= 22:
                print("Selamat malam! Semoga tidurmu nyenyak.")
            else:
                print("Waktu tidak valid.")
            if waktu == 'malam' and jam >= 22 and lokasi != 'rumah':
                print("Waktunya tidur, tapi kamu tidak di rumah. Pastikan untuk tidur dengan aman.")
            else:
                print("Masih ada waktu untuk beraktivitas.")
        elif waktu == 'pagi' and jam < 12:
            print("Selamat pagi! Semoga harimu menyenangkan.")
        elif waktu == 'siang' and jam >= 12 and jam < 18:
            print("Selamat siang! Semoga harimu produktif.")
            print("Waktu tidak valid.")
        else:
            print("Waktu tidak valid.")