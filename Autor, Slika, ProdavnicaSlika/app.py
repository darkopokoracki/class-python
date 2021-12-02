from typing import List


class Autor:
    __ime_prezime : str
    __godiste : int

    def __init__(self, ime_prezime: str, godiste: int) -> None:
        self.__ime_prezime = ime_prezime
        self.__godiste = godiste
    
    def get_ime_prezime(slef):
        return slef.__ime_prezime
    def set_ime_prezime(self, novo_ime_prezime):
        self.__ime_prezime = novo_ime_prezime

    def get_godiste(self):
        return self.__godiste
    def set_godiste(self, novo_godiste):
        self.__godiste = novo_godiste

    def __str__(self) -> str:
        res = f'Ime i prezim: {self.__ime_prezime}\n'
        res += f'Godiste: {self.__godiste}\n'

        return res


class Slika:
    __naziv_slike : str
    __autor : Autor
    __godina_slike : int
    __cena : float

    def __init__(self, naziv_slike: str, autor: Autor, godina_slike: int, cena: float) -> None:
        self.__naziv_slike = naziv_slike
        self.__autor = autor
        self.__godina_slike = godina_slike
        self.__cena = cena

    def get_naziv_slike(self):
        return self.__naziv_slike
    def set_naziv_slike(self, novi_naziv_slike):
        self.__naziv_slike = novi_naziv_slike

    def get_autor(self):
        return self.__autor
    def set_autor(self, novi_autor):
        self.__autor = novi_autor

    def get_godina_slike(self):
        return self.__godina_slike
    def set_godina_slike(self, nova_godina_slike):
        self.__godina_slike = nova_godina_slike

    def get_cena(self):
        return self.__cena
    def seet_cena(self, nova_cena):
        self.__cena = nova_cena

    def __str__(self) -> str:
        res = f'Naziv slike: {self.__naziv_slike}\n'
        res += f'Godina: {self.__godina_slike}\n'
        res += f'Cena: {self.__cena}\n'
        res += f'Autor: \n'
        res += f'Ime i prezime: {self.__autor.get_ime_prezime()}\n'
        res += f'Godiste: {self.__autor.get_godiste()}\n'

        return res

    def provera_autora(self, ime_autora):
        if self.__autor.get_ime_prezime() == ime_autora:
            return True
        else:
            return False

    def starost_slike(self):
        return 2021 - self.__godina_slike

    def provera_veka(self, vek):
        pocetak_veka = (vek * 100) - 99
        kraj_veka = vek * 100

        if self.__godina_slike >= pocetak_veka and self.__godina_slike <= kraj_veka:
            return True
        else:
            return False

class ProdavnicaSlika():
    lista_slika : list
    naziv : str
    adresa : str

    def __init__(self, lista_slika: list, naziv: str, adresa: str) -> None:
        self.lista_slika = lista_slika
        self.naziv = naziv
        self.adresa = adresa
    
    def najstarija_slika(self):
        if len(self.lista_slika) == 0:
            print("Nemamo ni jedu sliku u prodavnci")
            return None
        
        najstarija_slika = self.lista_slika[0]

        for slika in self.lista_slika:
            if slika.get_godina_slike() < najstarija_slika.get_godina_slike():
                najstarija_slika = slika
            
        print(najstarija_slika)
        return najstarija_slika


    def dodaj_novu_sliku(self, new_img):
        self.lista_slika.append(new_img)


    def ukupna_cena_slika(self):
        ukupna_cena = 0

        for slika in self.lista_slika:
            ukupna_cena += slika.get_cena()

        print(f"Ukupna cena: {ukupna_cena}")
        return ukupna_cena


    def lista_slika_iz_veka(self, vek):
        slike_u_veku = []

        for slika in self.lista_slika:
            if slika.provera_veka(vek):
                slike_u_veku.append(slika)

        return slike_u_veku


    def prosecna_starost_slika(self):
        suma_starosti_slika = 0

        for slika in self.lista_slika:
            suma_starosti_slika += slika.starost_slike()

        return suma_starosti_slika / len(self.lista_slika)


    def __str__(self) -> str:
        res = f'Naziv Prodavnice: {self.naziv}\n'
        res += f'Adresa: {self.adresa}\n'
        for slika in self.lista_slika:
            res += f'{"*" * 50}\n'
            res += f'\tNaziv slike: {slika.get_naziv_slike()}\n'
            res += f'\tGodina: {slika.get_godina_slike()}\n'
            res += f'\tCena: {slika.get_cena()}\n'
            res += f'\tAutor:\n'
            res += f'\t\tIme i prezime: {slika.get_autor().get_ime_prezime()}\n'
            res += f'\t\tGodiste: {slika.get_autor().get_godiste()}\n'
            res += f'{"*" * 50}\n'

        return res



#Glavni deo programa
#1. Rucno testiranje klasa i svih metoda klase ProdavnicaSlika
"""
autor1 = Autor('John Doe', 1923)
autor2 = Autor('Joe Paul', 1978)
autor3 = Autor('Toefil Mijir', 1866)

slika1 = Slika("Naziv1", autor1, 1950, 300000)
slika2 = Slika("Naziv2", autor1, 1956, 390000)
slika3 = Slika("Naziv3", autor2, 1990, 489000)
slika4 = Slika("Naziv4", autor3, 1890, 1000000000)
slika5 = Slika("Naziv5", autor3, 2001, 3000000000)

prodavnica1 = ProdavnicaSlika(
    [slika1, slika2, slika3, slika4, slika5], 'PhotoSelling', 'M. Pupina 44'
    )



prodavnica1.najstarija_slika()
nova_slika = Slika('Naziv6', autor2, 1992, 500000)
prodavnica1.dodaj_novu_sliku(nova_slika)
prodavnica1.ukupna_cena_slika()
prodavnica1.lista_slika_iz_veka(20)
prodavnica1.prosecna_starost_slika()

print(prodavnica1)
"""


prodavnice = []

n_prodavnica_slika = int(input("Unesite n prodavnica slika: "))
for i in range(n_prodavnica_slika):
    naziv_prodavnice = input(
        f"Unesite naziv za {i + 1}. prodavnicu: "
        )

    adresa_prodavnice = input(
        f"Unesite adresu za {i + 1}. prodavnicu: "
        )

    m_broj_slika = int(input(
        f"Unesite broj slika u {i + 1}. prodavnici: "
    ))

    m_slike = []
    for j in range(m_broj_slika):
        naziv_slike = input(
            f"Unesite naziv za {j + 1}. sliku: "
        )

        cena_slike = float(input(
            f"Unesite cenu za {j + 1}. sliku: "
        ))

        godina_slike = int(input(
            f"Unesite godinu slike za {j + 1}. sliku: "
        ))

        ime_prezime_autora = input(
            f"Unesite ime i prezime autora za {j + 1}. sliku: "
        )

        godiste_autora = int(input(
            f"Unesite godiste autora za {j + 1}. sliku: "
        ))

        autor = Autor(ime_prezime_autora, godiste_autora)
        slika = Slika(naziv_slike, autor, godina_slike, cena_slike)
        m_slike.append(slika)
    
    prodavnica = ProdavnicaSlika(m_slike, naziv_prodavnice, adresa_prodavnice)
    prodavnice.append(prodavnica)


najveca_vrednost_prodavnice = prodavnice[0]
for shop in prodavnice:
    if shop.ukupna_cena_slika() > najveca_vrednost_prodavnice.ukupna_cena_slika():
        najveca_vrednost_prodavnice = shop
    
print(
    f'Prodavnica koja ima najvecu vrednost sto se tice slika: {najveca_vrednost_prodavnice}'
)


