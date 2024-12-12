class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
        print(f"{montant} a été déposé. Votre nouveau solde: {self.solde}")

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            print(f"{montant} a été retiré. Votre nouveau solde: {self.solde}")
        else:
            print("Impossible de faire cette action!")

    def afficher_solde(self):
        print(f"Solde actuel: {self.solde}")

compte1 = CompteBancaire("Zouhair", 5000)
compte1.afficher_solde()
compte1.deposer(1000)
compte1.afficher_solde()
compte1.retirer(500)
compte1.afficher_solde()