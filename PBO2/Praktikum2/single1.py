class Kendaraan:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna
        
    def berkendara(self):
        print("Kendaraan ini sedang parkir.")
        
class SepedaMotor(Kendaraan):
    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc
        
    def belok(self):
        print("Sepeda motor ini sedang berjalan.")
        
motorA = SepedaMotor("Sepeda Motor", "kawasaki", "hijau", 250)
motorA.berkendara() # Output: Kendaraan ini sedang parkir.
motorA.belok() # Output: Sepeda motor ini sedang berjalan.