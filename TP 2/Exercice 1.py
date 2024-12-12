class Chien:
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age

    def aboyer(self):
        print("Woof!")

chien1 = Chien("Chien", "Pitbull", 3)
chien1.aboyer()