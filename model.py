class Turnir:
    def __init__(self, stevilo_skupin):
        self.stevilo_skupin = stevilo_skupin
        self.skupine = []


class Skupina:
    def __init__(self, indeks_skupine):
        self.ekipe = []
 


class Ekipa:
    def __init__(self, ime, seed1, ekskluzivni):
        self.ime = ime
        self.seed1 = seed1
        self.ekskluzivni = ekskluzivni
        self.odigrane_igre = []

    def dodaj_igro(self, winner, loser):
        igra = Igra(winner, loser)
        self.odigrane_igre.append(igra)


class Igra:
    def __init__(self, winner, loser):
        self.winner = winner
        self.loser = loser

        