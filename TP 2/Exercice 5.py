class Animal:
    def faire_du_bruit(self):
        print("L'animal fait un bruit.")

class Chien(Animal):
    def faire_du_bruit(self):
        print("Woof!")

class Chat(Animal):
    def faire_du_bruit(self):
        print("Miaou!")

animal1 = Animal()
animal1.faire_du_bruit()
chien2 = Chien()
chien2.faire_du_bruit()
chat1 = Chat()
chat1.faire_du_bruit()