print('\nFaldi Hirana\n190511011\nTI21B\n')
from playsound import playsound

class hewan:
    def __init__(self,hewan):
        self.hewan = hewan
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')

class gajah(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\Faldi Hirana Rusnadi\OneDrive\Documents\PBO2\sound\suara_gajah.mp3")

class ayam(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\Faldi Hirana Rusnadi\OneDrive\Documents\PBO2\sound\suara-anak-ayam-rombongan-iburung-com.mp3")

class gorilla(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\Faldi Hirana Rusnadi\OneDrive\Documents\PBO2\sound\suara-gorilla-menggeram.mp3")

class ular(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\Faldi Hirana Rusnadi\OneDrive\Documents\PBO2\sound\suara-desis-ular.mp3")

class kambing(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\Faldi Hirana Rusnadi\OneDrive\Documents\PBO2\sound\suara-cempe-anak-kambing.mp3")

class elang(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\Faldi Hirana Rusnadi\OneDrive\Documents\PBO2\sound\suara-burung-elang-hawk.mp3")

class bebek(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\Faldi Hirana Rusnadi\OneDrive\Documents\PBO2\sound\suara-bebek.mp3")

class badak(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\Faldi Hirana Rusnadi\OneDrive\Documents\PBO2\sound\suara-badak.mp3")

class babi(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\Faldi Hirana Rusnadi\OneDrive\Documents\PBO2\sound\suara-babi.mp3")

class angsa(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\Faldi Hirana Rusnadi\OneDrive\Documents\PBO2\sound\suara-angsa-banyak.mp3")

def hewan_bersuara(hewan):
    hewan.bersuara()

hewan0 = hewan('Hewan')
hewan1 = gajah('gajah')
hewan2 = ayam('ayam')
hewan3 = gorilla('gorilla')
hewan4 = ular('ular')
hewan5 = kambing('kambing')
hewan6 = elang('elang')
hewan7 = bebek('bebek')
hewan8 = badak('badak')
hewan9 = babi('babi')
hewan10 = angsa('angsa')

hewan_bersuara(hewan0)
hewan_bersuara(hewan1)
hewan_bersuara(hewan2)
hewan_bersuara(hewan3)
hewan_bersuara(hewan4)
hewan_bersuara(hewan5)
hewan_bersuara(hewan6)
hewan_bersuara(hewan7)
hewan_bersuara(hewan8)
hewan_bersuara(hewan9)
hewan_bersuara(hewan10)
