class List_film:
    def __init__(self,tanggal):
        self.tanggal = tanggal
        self.list = List()
    
    def tampil(self):
        print('\t\t\tFilm List\t\t\t\n','\t','='*37,'\t')
        print(f'Date\t\t:  {self.tanggal}\n')

class Film:
    def __init__(self,judul,genre,tayang,sutradara):
        self.judul = judul
        self.genre = genre
        self.tayang = tayang
        self.sutradara = sutradara

    def get_judul(self):
        return self.judul
    def get_genre(self):
        return self.genre
    def get_tayang(self):
        return self.tayang
    def get_sutradara(self):
        return self.sutradara

class List:
    def __init__(self):
        self.aFilm = []

    def add_film(self,film):
        self.aFilm.append(film)

    def daftar_film(self):
        for film in self.aFilm:
            print(f'Judul\t\t: ',film.judul)
            print(f'Genre\t\t: ',film.genre)
            print(f'Tayang\t\t: ',film.tayang)
            print(f'sutradara\t\t: ',film.sutradara,'\n')

listApril = List_film('April 2023')
film1 = Film('THE SUPER MARIO BROS', 'Animation, Adventure, Comedy', 'Senin Pukul 22.00', 'Michael Jelenic')
film2 = Film('JOHN WICK', 'Action, Crime, Thriller', 'Selasa Pukul 21.50', 'Chad Stahelski')
listApril.list.add_film(film1)
listApril.list.add_film(film2)
listApril.list.aFilm
listApril.tampil()
listApril.list.daftar_film()