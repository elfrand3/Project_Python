class tabungan :
    def __init__(self, dosen, ku, keren):
        self.dosen = dosen
        self.ku = ku
        self.keren = keren
    
    def setoran(self, keren):
        self.keren = keren
    def penarikan(self, keren):
        self.keren = keren

    def info(self):
        print('Nomer rekening = ',self.dosen)
        print('Nama Nasabah = ',self.ku)
        print('saldo = ',self.keren)

#program

adi = tabungan('6501200101','Adi Wijaya','50000')
adi.setoran(100000)
adi.info()
adi.penarikan(25000)
adi.info()