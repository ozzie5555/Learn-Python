nama = input("Masukkan nama Anda: ")
team = input("Masukkan nama tim Anda: ")

if nama.strip() != "":
    print("Nama Anda adalah:", nama)
else:
    print("Nama tidak boleh kosong.")

if team.strip() != "":
    print("Nama tim Anda adalah:", team)
else:
    print("Nama tim tidak boleh kosong.")

print("Terima kasih telah mendaftar untuk CTF!")