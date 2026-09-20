# Program mengecek apakah sebuah bilangan prima

def cek_prima(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

angka = [2, 3, 4, 5, 7, 9, 11, 15]

for a in angka:
    if cek_prima(a):
        print(a, "adalah bilangan prima")
    else:
        print(a, "bukan bilangan prima")