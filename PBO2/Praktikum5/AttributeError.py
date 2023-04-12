class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

mahasiswa = Mahasiswa("Faldi Hirana R", 190511011)

try:
    print(mahasiswa.alamat)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")