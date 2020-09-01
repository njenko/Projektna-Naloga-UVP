class Turnir:
    def __init__(self, stevilo_skupin, nacin_igranja):
        self.stevilo_skupin = stevilo_skupin
        self.nacin_igranja = nacin_igranja
        self.seznam_skupin = []
        self.seznam_ekip = []


#nacin_igranja = 1 - single round robin, = 2 - double round robin

class Skupina:
    def __init__(self, indeks_skupine):
        self.ekipe_v˜_skupini = []

    def dodaj_ekipo(self, ime, seed1, ekskluzivni_kriterij):
        nova_ekipa = Ekipa(ime,seed1, ekskluzivni_kriterij)
        elf.ekipe_v_skupini.append(nova_ekipa)


    def zakljucena_skupina(self, nacin_igranja):
        if len(seznam_ekip) < 1:
            pass
        else:
            ekipe_koncane = 0
            for i in range len(seznam_ekip):
                if len(seznam_ekip[i].odigrane_igre) < (len(seznam_ekip) - 1) * nacin_igranja: #vsaka ekipa igra z vsemi ostalimi (zato -1), ce igra 2x potem je pomnozena z 2
                    pass
                else:
                    ekipe_koncane =+ 1
        if len(seznam_ekip) = ekipe_koncane:
            return True
        else:
            return False


class Ekipa:
    def __init__(self, ime, seed1, ekskluzivni_kriterij):
        self.ime = ime
        self.seed1 = seed1
        self.ekskluzivni_kriterij = ekskluzivni_kriterij
        self.odigrane_igre = []

    def dodaj_igro(self, winner, loser):
        igra = Igra(winner, loser)
        self.odigrane_igre.append(igra)

    def izracunaj_tocke_ekipe(self):
        st_tock = 0
        for i in range len(odigrane_igre):
            if odigrane_igre[i].winner == ime:
                st_tock =+ 1
            else:
                pass



class Igra:
    def __init__(self, winner, loser):
        self.winner = winner
        self.loser = loser

        