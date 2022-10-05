import random
VALEURS = ['','As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
COULEURS = ['', 'pique', 'coeur', 'carreau', 'trefle']

class Carte:
    """Initialise couleur (de 1 à 4), et valeur (de 1 à 13)"""

    def __init__(self, couleur , valeur):
        self.couleur = couleur
        self.valeur = valeur

    def get_nom(self):
        """Renvoie le nom de la Carte As, 2, ... 10, Valet, Dame, Roi"""
        return VALEURS[self.valeur]

    def get_couleur(self):
        """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle)"""
        return COULEURS[self.couleur]

    def comparer_carte(self):
        """ Renvoie la carte la plus forte"""
        if paquet_1.contenu[0].valeur > paquet_2.contenu[0].valeur :
            print("La carte du paquet_1 est supérieur à la carte du paquet_2")
        elif paquet_1.contenu[0].valeur > paquet_2.contenu[0].valeur :
            print("La carte du paquet_1 est égale à la carte du paquet_2")
        else:
            print("La carte du paquet_1 est supérieur à la carte du paquet_2")


class PaquetDeCarte:
    """Initialise un paquet de cartes, avec un attribut contenu, de type list, vide"""

    def __init__(self):
        self.contenu = []

    def remplir(self):
        """Remplit le paquet de cartes : en parcourant les couleurs puis les valeurs"""
        self.contenu = [Carte(couleur, valeur) for couleur in range(1, 5) for valeur in range(1, 14)]


    def get_carte_at(self, pos):
        """Renvoie la Carte qui se trouve à la position donnée"""
        if 0 <= pos < 52:
            return self.contenu[pos]

    def afficher_carte52(self):
        """ permet d'afficher les cartes du paquet 1"""
        for valeur in range(len(paquet_52.contenu)):
            print(paquet_52.contenu[valeur].get_nom() , paquet_52.contenu[valeur].get_couleur())

    def afficher_carte1(self):
        """ permet d'afficher les cartes du paquet 1"""
        for valeur in range(len(paquet_1.contenu)):
            print(paquet_1.contenu[valeur].get_nom() , paquet_1.contenu[valeur].get_couleur())

    def afficher_carte2(self):
        """ permet d'afficher les cartes du paquet 2"""
        for valeur in range(len(paquet_2.contenu)):
            print(paquet_2.contenu[valeur].get_nom() , paquet_2.contenu[valeur].get_couleur())

    def afficher_main(self):
        """ permet d'afficher les cartes de la main"""
        nombre = 1
        for valeur in range(len(la_main.contenu)):
            print(la_main.contenu[valeur].get_nom() , la_main.contenu[valeur].get_couleur() , "carte", nombre)
            nombre += 1


    def tirer_carte(self):
        """ permet de tirer une carte depuis le paquet"""
        pack = []
        pack.append(paquet_52.contenu[valeur])
        print(pack[0].get_nom() ,pack[0].get_couleur() )

    def melanger_carte(self):
        """ permet de melanger le paquet"""
        random.shuffle(paquet_52.contenu)

    def distribuer_carte(self):
        for i in range(52):
            if 26 >  i :
                paquet_1.contenu.append((paquet_52.contenu[i]))
            if i >= 26  :
                paquet_2.contenu.append((paquet_52.contenu[i]))

    def distribuer_la_main(self):
        for i in range(3):
            la_main.contenu.append(paquet_1.contenu[i])
            la_main.contenu.append(paquet_2.contenu[i])


def affrontement():
    for valeurs in range(3):
        comparer_carte()
        if paquet_1.contenu[0].valeur > paquet_2.contenu[0].valeur :
            paquet_1.contenu.append(la_main.contenu[0])
            paquet_1.contenu.append(la_main.contenu[1])
            del(paquet_1.contenu[0])
            del(paquet_2.contenu[0])
        elif paquet_1.contenu[0].valeur == paquet_2.contenu[0].valeur :
            if paquet_1.contenu[2].valeur > paquet_2.contenu[2].valeur:
                for i in range(3):
                    paquet_1.contenu.append(paquet_2.contenu[0])
                    paquet_1.contenu.append(paquet_1.contenu[0])
                    del(paquet_2.contenu[0])
                    del(paquet_1.contenu[0])
            else:
                for i in range(3):
                    paquet_2.contenu.append(paquet_2.contenu[0])
                    paquet_2.contenu.append(paquet_1.contenu[0])
                    del(paquet_2.contenu[0])
                    del(paquet_1.contenu[0])
        else:
            paquet_2.contenu.append(la_main.contenu[0])
            paquet_2.contenu.append(la_main.contenu[1])
            del(paquet_1.contenu[0])
            del(paquet_2.contenu[0])
        del(la_main.contenu[0])
        del (la_main.contenu[0])

def comparer_carte():
        """ Renvoie la carte la plus forte"""
        if paquet_1.contenu[0].valeur > paquet_2.contenu[0].valeur :
            print("La carte du paquet_1 est supérieur à la carte du paquet_2")
        elif paquet_1.contenu[0].valeur == paquet_2.contenu[0].valeur :
            print("La carte du paquet_1 est égale à la carte du paquet_2")
        else:
            print("La carte du paquet_1 est inférieur à la carte du paquet_2")


def nombre_carte():
    print("paquet_1 nombre de carte :" , len(paquet_1.contenu))
    print("paquet_2 nombre de carte :" , len(paquet_2.contenu))




paquet_52 = PaquetDeCarte()
paquet_1 = PaquetDeCarte()
paquet_2 = PaquetDeCarte()
la_main = PaquetDeCarte()
paquet_52.remplir()
paquet_52.melanger_carte()
paquet_1.distribuer_carte()
la_main.distribuer_la_main()
print("-------------------------la_main-------------------------")
la_main.afficher_main()
affrontement()
print("-------------------------paquet_1-------------------------")
paquet_1.afficher_carte1()
print("-------------------------paquet_2-------------------------")
paquet_2.afficher_carte2()
nombre_carte()