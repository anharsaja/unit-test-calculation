import os
os.system('cls')

class kalkulator:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def penjumlahan(self):
        return self.a + self.b

    def pengurangan(self):
        return self.a - self.b

    def perkalian(self):
        return self.a * self.b

    def pembagian(self):
        if self.b == 0:
            raise ValueError(
                f'Hasil operasi dari {self.a} / {self.b} = Tak Terhingga')
        return self.a / self.b


def hasil(operasi, angka1, angka2):
    hasil = kalkulator(angka1, angka2)
    if operasi == "1":
        operasi = "+"
        hasil = hasil.penjumlahan()
    elif operasi == '2':
        operasi = "-"
        hasil = hasil.pengurangan()
    elif operasi == '3':
        operasi = "*"
        hasil = hasil.perkalian()
    elif operasi == '4':
        operasi = "/"
        hasil = hasil.pembagian()
    else:
        return 'Tidak valid'
    return f'Hasil operasi dari {angka1} {operasi} {angka2} = {hasil}'

def show():
    print('='*30)
    print('\t  Kalkulator')
    print('='*30)
    print('   1. Penjumlahan \t [+]')
    print('   2. Pengurangan \t [-]')
    print('   3. Perkalian \t [*]')
    print('   4. Pembagian \t [/]')
    print('=' * 30)
    operasi = input('Pilih operasi (1/2/3/4): ')
    angka1 = int(input('Masukkan bilangan pertama: '))
    angka2 = int(input('Masukkan bilangan kedua: '))
    print('=' * 30)
    print(hasil(operasi, angka1, angka2))


if __name__ == '__main__':
    show()