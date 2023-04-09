
class Jurnal:
    def __init__(self,title,date):
        self.title = title
        self.date = date

class peneliti:
    def __init__(self,nama,jurnal):
        self.nama = nama
        self.jurnal = jurnal

    def daftar_jurnal(self):
        print(f'\nPeneliti\t:  {self.nama}\n')
        for jurnal in self.jurnal:
            print(f'Judul\t\t: ',jurnal.title)
            print(f'Published\t:  {jurnal.date}')
           
jurnal1 = Jurnal('SISTEM INFORMASI LEGALISIR ONLINE UNTUK MAS TAHFIDZ YANBUUL QURAN', 2020)
peneliti1 = peneliti('Mukhammad Irfan Syauqi', [jurnal1])
jurnal2 = Jurnal('Implementasi E-Legalisir Uantuk Legalisir Ijazah dan Transkrip Online pada Fakultas Ilmu ', 2020)
peneliti2 = peneliti('Yudha Permana, Herry Derajad Wijaya ', [jurnal2])
peneliti1.daftar_jurnal()
peneliti2.daftar_jurnal()
 