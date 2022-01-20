print()
print("..... Love you sayang .....")
print()
print("Nama = el_codee")
print("ID  = 00001")
print()
a = int(input("Masukkan Harga-1 = Rp "))
b = int(input("Masukkan Harga-2 = Rp "))
c = int(input("Masukkan Harga-3 = Rp "))
print()
Total = a + b + c
Potongan = Total - 10000
for i in range(3):
    if Total > 50000:
        TA = Total - 10000
        print("Total    = Rp",Total)
        print("Potongan = Rp 10000")
        print("Bayar    = Rp",Potongan)
    else:
        TA = Total - 0
        print("Total    = Rp",Total)
        print("Potongan = Rp 0")
        print("Bayar    = Rp",Total)
print()
print(".... Sampai jumpa kembali ....")
print()
