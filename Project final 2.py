from tkinter import*
import tkinter as tk
import time
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
        elif paquet_1.contenu[0].valeur == paquet_2.contenu[0].valeur :
            print("La carte du paquet_1 est égale à la carte du paquet_2")
        else:
            print("La carte du paquet_1 est supérieur à la carte du paquet_2")

    def image(self) :
            """
            méthode permettant l'affichage d'une carte"
            """
            longeur_paquet_1 = "paquet_1 longeur = " , len(paquet_1.contenu) - 1
            longeur_paquet_2 = "paquet_2 longeur = "  , len(paquet_2.contenu) - 1
            fichier_fond = "tapis_vert.png"
            fichier_paquet_1 = "cartes/"+ str(paquet_1.contenu[0].valeur) + str(paquet_1.contenu[0].couleur) +".GIF"
            fichier_paquet_2 = "cartes/"+ str(paquet_2.contenu[0].valeur) + str(paquet_2.contenu[0].couleur) +".GIF"
            fichier_tapis_joueur_1 = "carte_joueur1.png"
            fichier_tapis_joueur_2 = "carte_joueur2.png"
            fenetre = tk.Tk()
            fenetre.geometry('2000x1000')
            fenetre['background']='#008c42'
            #afficher le fond
            image_carte_fond = tk.PhotoImage( file = fichier_fond )
            label_fond = tk.Label( fenetre , image = image_carte_fond )
            label_fond.place(x= 250, y= 60)
            #afficher le tapis du joueur 1
            image_tapis_joueur_1 = tk.PhotoImage( file = fichier_tapis_joueur_1 )
            label_tapis_joueur_1 = tk.Label( fenetre , image = image_tapis_joueur_1 )
            label_tapis_joueur_1.place(x= 500, y= 600)
            #afficher le tapis du joueur 2
            image_tapis_joueur_2 = tk.PhotoImage( file = fichier_tapis_joueur_2 )
            label_tapis_joueur_2 = tk.Label( fenetre , image = image_tapis_joueur_2 )
            label_tapis_joueur_2.place(x= 1167, y= 600)
            #afficher la carte du paquet
            image_1 = tk.PhotoImage( file = fichier_paquet_1 )
            label_1 = tk.Label( fenetre , image = image_1 )
            label_1.place(x= 500, y= 200)
            #afficher la carte du paquet_2
            image_2 = tk.PhotoImage( file = fichier_paquet_2 )
            label_2 = tk.Label( fenetre , image = image_2 )
            label_2.place(x= 1167, y= 200)
            #score des paquets
            button_paquet_1 = Button( fenetre, text = longeur_paquet_1 )
            button_paquet_1.place(x= 1368, y= 700)
            button_paquet_1.pack(pady = 10)
            button_paquet_2 = Button( fenetre, text = longeur_paquet_2 )
            button_paquet_2.place(x= 301, y= 700)
            button_paquet_2.pack(pady = 10)
            fenetre.after(2000,lambda:fenetre.destroy())
            fenetre.mainloop()
            


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
        if len(paquet_1.contenu) == 0:
            print("paquet_1 vide")

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
        """ permet de melanger le paquet"""   #permet de mélanger le paquet de manière aléatoire
        for i in range(10):
            random.shuffle(paquet_52.contenu)

    def distribuer_carte(self):
        """ distribue les 52 cartes du paquet_52 équitablement dans le paquet_1 et le paquet_2 """
        for i in range(52):
            if 26 >  i :
                paquet_1.contenu.append((paquet_52.contenu[i]))
            if i >= 26  :
                paquet_2.contenu.append((paquet_52.contenu[i]))

    def distribuer_la_main(self):
        """ permet d'avoir des cartes dans la main"""
        la_main.contenu.append(paquet_1.contenu[0])
        la_main.contenu.append(paquet_2.contenu[0])




def affrontement():
    """ permet de jouer a la bataille"""
    while not len(paquet_1.contenu) == 0 or len(paquet_2.contenu) == 0 :         # la partie s'arrète lorsque l'un des deux paquets n'est plus de cartes
        print("-------------------------la_main-------------------------")
        la_main.distribuer_la_main()
        la_main.afficher_main()
        comparer_carte()
        if paquet_1.contenu[0].valeur > paquet_2.contenu[0].valeur : # si la valeur de la carte du paquet 1 est plus grande que la carte du paquet 2 alors suprimer la carte de la main et ajouter la carte aux paquet 1
            paquet_1.contenu.append(la_main.contenu[0])
            paquet_1.contenu.append(la_main.contenu[1])
            carte.image()
            del(paquet_1.contenu[0])
            del(paquet_2.contenu[0])
        elif paquet_1.contenu[0].valeur == paquet_2.contenu[0].valeur :          # si la valeur de la carte des deux paquets est égale
            if len(paquet_1.contenu) <= 2 or len(paquet_2.contenu) <= 2 :        # Arreter le jeu lorsque qu'il reste deux cartes dans l'un des paquets
                print("partie terminer")
                carte.image()
            if paquet_1.contenu[2].valeur > paquet_2.contenu[2].valeur:          # tirer la troisième cartes pour les départager
                for i in range(3):
                    paquet_1.contenu.append(paquet_2.contenu[0])
                    paquet_1.contenu.append(paquet_1.contenu[0])
                    carte.image()
                    del(paquet_2.contenu[0])
                    del(paquet_1.contenu[0])
            else:
                for i in range(3):
                    paquet_2.contenu.append(paquet_2.contenu[0])
                    paquet_2.contenu.append(paquet_1.contenu[0])
                    carte.image()
                    del(paquet_2.contenu[0])
                    del(paquet_1.contenu[0])
        else:
            paquet_2.contenu.append(la_main.contenu[0])
            paquet_2.contenu.append(la_main.contenu[1])
            carte.image()
            del(paquet_2.contenu[0])
            del(paquet_1.contenu[0])
        nombre_carte()  
        del(la_main.contenu[0])
        del (la_main.contenu[0])
        if len(paquet_1.contenu) == 0 or len(paquet_2.contenu) == 0 :
            print("partie terminer")
            

def comparer_carte():
        """ Renvoie la carte la plus forte"""
        if paquet_1.contenu[0].valeur > paquet_2.contenu[0].valeur :
            print("La carte du paquet_1 est supérieur à la carte du paquet_2")
        elif paquet_1.contenu[0].valeur == paquet_2.contenu[0].valeur :
            print("La carte du paquet_1 est égale à la carte du paquet_2")
        else:
            print("La carte du paquet_1 est inférieur à la carte du paquet_2")


def nombre_carte():
    """ permet de calculer le nombre de carte"""
    print("paquet_1 nombre de carte :" , len(paquet_1.contenu))
    print("paquet_2 nombre de carte :" , len(paquet_2.contenu))
    

carte = Carte(1 , 1)
paquet_52 = PaquetDeCarte()
paquet_1 = PaquetDeCarte()
paquet_2 = PaquetDeCarte()
la_main = PaquetDeCarte()
paquet_52.remplir()
paquet_52.melanger_carte()
paquet_1.distribuer_carte()

affrontement()
print("-------------------------paquet_1-------------------------")
paquet_1.afficher_carte1()
print("-------------------------paquet_2-------------------------")
paquet_2.afficher_carte2()
