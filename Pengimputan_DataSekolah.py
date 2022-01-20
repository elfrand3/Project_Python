class Sekolah:
    def __init__(self, inputkegiatan, inputpelaksana, inputwaktu, inputtempat):
        self.macam = inputkegiatan
        self.pelaksana = inputpelaksana
        self.waktu = inputwaktu
        self.tempat = inputtempat


kegiatan1 = Sekolah(
    "Ekstrakurikuler", "Semua Siswa dengan Bakat dan Minat Siswa", "010.00", "Halaman ")
kegiatan2 = Sekolah("Senam Pagi", "Semua Siswa",
                    "10.00-Selesai", "Halaman Sekolah")
kegiatan3 = Sekolah("Pramuka", "Semua Siswa", "11.00-12.00", "Halaman Sekolah")
kegiatan4 = Sekolah("Pelaksanaan Bansos", "Sebagian Siswa",
                    "13.00 - Selesai", "Kelas")
kegiatan5 = Sekolah("kegiatan les sekolah", "Seluruh Siswa",
                    "15.00 - Selesai", "Kelas")
print()

print("===========================KEGIATAN-KEGIATAN SEKOLAH===========================")
print("\nKegiatan = ", kegiatan1.__dict__)
print("\nKegiatan = ", kegiatan2.__dict__)
print("\nKegiatan = ", kegiatan3.__dict__)
print("\nkegiatan =",  kegiatan4.__dict__)
print("\nkegiatan =",  kegiatan5.__dict__)

print("===========================MACAM-MACAM KEGIATAN SEKOLAH===========================")
print("- Kegiatan", kegiatan1.macam)
print("- Kegiatan", kegiatan2.macam)
print("- Kegiatan", kegiatan3.macam)
print("- Kegiatan", kegiatan4.macam)
print("- Kegiatan", kegiatan5.macam)
print()

print("===========================TEMPAT DAN WAKTU===========================")
print("- Kegiatan" + kegiatan1.macam + " di " +
      kegiatan1.tempat + "Pada Jam" + kegiatan1.waktu)
