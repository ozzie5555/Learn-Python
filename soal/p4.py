# Program login dengan batas percobaan

username_benar = "admin"
password_benar = "12345"

percobaan = 0
maks_percobaan = 3
login_berhasil = False

while percobaan < maks_percobaan:
    print("Percobaan ke-", percobaan + 1)
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == username_benar and password == password_benar:
        login_berhasil = True
        break
    else:
        print("Username atau password salah!")
        percobaan = percobaan + 1

if login_berhasil = True:
    print("Selamat datang,", username)
else:
    print("Akun terkunci. Coba lagi nanti.")