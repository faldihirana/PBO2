class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
    def info(self):
        print(f"Mobil {self.merk} berwarna {self.warna} \n")

mobilA = Mobil("VW Kodok", "Pearl White")
mobilA.info() # Output: Mobil VW berwarna Pearl White