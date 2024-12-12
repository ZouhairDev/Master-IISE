class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans.")

    def ajouter_ami(self, ami):
        self.amis.append(ami)
        print(f"{ami.prenom} {ami.nom} a été ajouté comme ami.")

    def afficher_amis(self):
        print("Liste des amis:")
        for ami in self.amis:
            print(f"- {ami.prenom} {ami.nom}")

personne2 = Personne("nom1", "prenom1", 22)
personne3 = Personne("nom2", "prenom2", 23)
personne2.ajouter_ami(personne3)
personne2.afficher_amis()
