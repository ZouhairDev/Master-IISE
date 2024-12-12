class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Livre ajouté: {livre.titre} par {livre.auteur}")

    def afficher_livres(self):
        for livre in self.livres:
            print(f"{livre.titre}, par {livre.auteur} ({livre.annee_publication})")

bibliotheque = Bibliotheque()
livre1 = Livre("titre1", "auteur1", 2000)
livre2 = Livre("titre2", "auteur2", 2001)
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.afficher_livres()