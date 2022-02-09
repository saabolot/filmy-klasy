
class Film():
    def __init__(self, tytuł, rok_wydania, gatunek):
        self.tytuł = tytuł
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzeń = 0

    def play(self, odtw = 1):
        self.liczba_odtworzeń += odtw
    
    def __str__(self):
        return f'{self.tytuł} ({self.rok_wydania})'
    

class Serial(Film):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(* args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu
        self.liczba_odtworzeń = 0

    def play(self, odtw = 1):
        self.liczba_odtworzeń += odtw
    
    def __str__(self):
        return f'{self.tytuł} S{self.numer_sezonu}E{self.numer_odcinka}'

def get_movies():
    filmy = [i for i in Film if isinstance(i, Film) and not isinstance(i, Serial)]
    filmy_alfabetycznie = sorted(filmy key=     )
    print(filmy_alfabetycznie)
        
def get_series():
    seriale = [x for x in Serial if isinstance(x, Serial)]
    seriale_alfabetycznie = sorted(seriale key=  )
    print(seriale_alfabetycznie)

def search():


def generate_view():


def top_titles():