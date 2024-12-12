class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans.")

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule

    def etudier(self):
        print(f"L'étudiant {self.prenom} {self.nom} étudie actuellement.")

personne1 = Personne("Assafi", "Zouhair", 22)
personne1.se_presenter()
etudiant1 = Etudiant("Bendada", "Ashraf", 22, "3334")
etudiant1.se_presenter()
etudiant1.etudier()