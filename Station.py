class Station:
    def __init__(self, nom, lien, cm_neige, cm_tomber):
        self.nom = nom
        self.lien = lien
        self.cm_neige = cm_neige
        self.cm_tomber = cm_tomber

    def display(self):
        print(self.nom, " neige tomber: ", self.cm_tomber, "neige en haut : ", self.cm_neige)

    def analyse_station(self):
        if "/" in self.cm_tomber:
            self.cm_tomber = 0

    def set_cm_tomber(self, value):
        self.cm_tomber = value

    def list(self):
        return self.nom+" "+self.lien+" "+"cm neige en haut"+self.cm_neige+" neige tomber "+self.cm_tomber
