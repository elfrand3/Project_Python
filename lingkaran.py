class lingkaran:
    def __init__(self, r):
        self.jari2 = r

    def getluas(self):
        return (3.14 * self.jari2 * self.jari2)


class tabung(lingkaran):
    def __init__(self, r, t):
        super().__init__(r)
        self.tinggi = t
    def getvolume(self):
        return (super().getluas() * self.tinggi)

basoka = tabung ( 6, 5)
print('Luas Atas lingkaran = ', basoka.getluas())
print('Volume Basoka = ', basoka.getvolume())

r = float(input('Masukkan jari2 = '))
t = float(input('Masukkan tinggi = '))
basoka = tabung ( r, t)
print('Luas Atas lingkaran = ', basoka.getluas())
print('Volume Basoka = ', basoka.getvolume())