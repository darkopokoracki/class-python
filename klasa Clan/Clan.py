class Clan:
    __ime : str
    __tezina : float
    __visina: float

    def __init__(self, ime: str, tezina: float, visina: float) -> None:
        self.__ime = ime
        self.__tezina = tezina
        self.__visina = visina

    #Getter i Setter za IME
    def get_ime(self):
        return self.__ime
    def set_ime(self, novo_ime):
        self.__ime = novo_ime

    #Getter i Setter za TEZINU
    def get_tezina(self):
        return self.__tezina
    def set_tezina(self, nova_tezina):
        self.__tezina = nova_tezina
    
    #Getter i Setter za VISINU
    def get_visina(self):
        return self.__visina
    def set_visina(self, nova_visina):
        self.__visina = nova_visina

    def __str__(self) -> str:
        res = f"Ime: {self.__ime}\n"
        res += f"Tezina: {self.__tezina}\n"
        res += f"Visina: {self.__visina}\n"
        return res

    def itm(self):
        index = (self.__tezina * 10000) / (self.__visina * self.__visina)
        return index

    def program(self):
        if self.itm() > 25:
            return "Kardio"
        else: 
            return "Individualno"
    

class Student(Clan):
    prosek : float

    def __init__(self, ime: str, tezina: float, visina: float, prosek: float) -> None:
        super().__init__(ime, tezina, visina)
        self.prosek = prosek

    def __str__(self) -> str:
        return super().__str__() + f"Prosek: {self.prosek}"

    def clanarina(self):
        print(f"{self.get_ime()} preporucujemo vam program {self.program()}")
        
        if self.program() == 'Kardio':
            cena_termina = 700
            broj_programa = int(input("unesite broj programa, 8 ili 12: "))

            if broj_programa == 8:
                iznos = broj_programa * cena_termina

            if broj_programa == 12:
                iznos = broj_programa * cena_termina


        if self.program() == 'Individualno':
            print("Unesite zeljeni deo dana: ")
            print("C = Ceo dan\nPR = Pre podne")
            deo_dana = input("Vas izbor: ").upper()

            if deo_dana == "C":
                cena_termina = 4000
                iznos = cena_termina

            if deo_dana == "PR":
                cena_termina = 2000
                iznos = cena_termina

        if self.prosek > 8:
            iznos = (85 * iznos) / 100

        print(f"Treba da platite: {iznos}")
        return iznos

class Regularni(Clan):
    kategorija : str

    def __init__(self, ime: str, tezina: float, visina: float, kategorija: str) -> None:
        super().__init__(ime, tezina, visina)
        self.kategorija = kategorija

    def __str__(self) -> str:
        return super().__str__() + f"Kategorija: {self.kategorija}"

    def clanarina_regularnog(self):
        print(f"{self.get_ime()} preporucujemo vam program {self.program()}")

        if self.program() == 'Kardio':
            cena_termina = 700
            broj_termina = int(input("Unesite broj termina, 8 ili 16: "))

            if broj_termina == 8:
                iznos = broj_termina * cena_termina

            if broj_termina == 16:
                iznos = broj_termina * cena_termina

        if self.program() == 'Individualno':
            if self.kategorija == 'Z':
                cena_termina = 6000
                iznos = cena_termina

            if self.kategorija == "NZ":
                cena_termina = 4000
                iznos = cena_termina

        print(f"Treba da platite: {iznos}")
        return iznos


class RegularniSaPrivilegijama(Clan):
    popust : int

    def __init__(self, ime: str, tezina: float, visina: float, popust: int) -> None:
        super().__init__(ime, tezina, visina)
        self.popust = popust

    def __str__(self) -> str:
        return super().__str__() + f"Popust: {self.popust}"
    
    def clanarina_privilegovanog(self):
        print(f"{self.get_ime()} preporucujemo vam program {self.program()}")

        if self.program() == 'Kardio':
            cena_termina = 700
            broj_termina = int(input("Unesite broj termina, 8 ili 16: "))

            if broj_termina == 8:
                iznos = broj_termina * cena_termina

            if broj_termina == 16:
                iznos = broj_termina * cena_termina

        if self.program() == 'Individualno':
            unos_zaposleni = input("Unesite Z il NZ: ").upper()

            if unos_zaposleni == 'Z':
                cena_termina = 6000
                iznos = cena_termina

            if unos_zaposleni == "NZ":
                cena_termina = 4000
                iznos = cena_termina

        iznos = ((100 - self.popust) * iznos) / 100
        return iznos


osoba1 = RegularniSaPrivilegijama("Darko", 80, 186, 50)
osoba1.clanarina_privilegovanog()
