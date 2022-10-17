# Projet de Bataille de MACABRE Mahël TG8 et GAYDU Dénys TG8 NSI/TERMINALE 2022/2023
from tkinter import*
import tkinter as tk
import time
import random

VALEURS = ['','', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi','As']
COULEURS = ['', 'pique', 'coeur', 'carreau', 'trefle']

class Carte:
    """Initialise couleur (de 1 à 4), et valeur (de 2 à 15)"""

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
        self.contenu = [Carte(couleur, valeur) for couleur in range(1, 5) for valeur in range(2, 15)]


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
            print("Victoire Du joueur 2")
        if len(paquet_1.contenu) < 3 and len(paquet_1.contenu) != 0 and paquet_1.contenu[0].valeur == paquet_2.contenu[0].valeur :
            for valeur in range(len(paquet_1.contenu)):
                print(paquet_1.contenu[valeur].get_nom() , paquet_1.contenu[valeur].get_couleur())
            print("Victoire Du joueur 2")

    def afficher_carte2(self):
        """ permet d'afficher les cartes du paquet 2"""
        for valeur in range(len(paquet_2.contenu)):
            print(paquet_2.contenu[valeur].get_nom() , paquet_2.contenu[valeur].get_couleur())
        if len(paquet_2.contenu) == 0:
            print("paquet_2 vide")
            print("Victoire Du joueur 1")
        if len(paquet_2.contenu) < 3 and len(paquet_2.contenu) != 0 and paquet_1.contenu[0].valeur == paquet_2.contenu[0].valeur :
            for valeur in range(len(paquet_1.contenu)):
                print(paquet_2.contenu[valeur].get_nom() , paquet_2.contenu[valeur].get_couleur())
            print("Victoire Du joueur 1")


    def tirer_carte(self):
        """ permet de tirer une carte depuis le paquet"""
        pack = []
        pack.append(paquet_52.contenu[valeur])
        print(pack[0].get_nom() ,pack[0].get_couleur() )

    def melanger_carte(self):
        """ permet de melanger le paquet"""   #permet de mélanger le paquet de manière aléatoire
        for i in range(3):
            random.shuffle(paquet_52.contenu)
            random.shuffle(paquet_52.contenu)

    def distribuer_carte(self):
        """ distribue les 52 cartes du paquet_52 équitablement dans le paquet_1 et le paquet_2 """
        #boucle de 52 tour
        for i in range(52):
            #si i est inferieur a 26
            if 26 >  i :
                paquet_1.contenu.append((paquet_52.contenu[i]))
            #sinon
            else:
                paquet_2.contenu.append((paquet_52.contenu[i]))

def affrontement():
    """ permet de jouer a la bataille"""
    conteur = 1
    while len(paquet_1.contenu) != 0 or len(paquet_2.contenu) != 0 :         # la partie s'arrète lorsque l'un des deux paquets n'est plus de cartes
        print("-------------------------carte posé-------------------------")
        comparer_carte()
        print(paquet_1.contenu[0].get_nom() , paquet_1.contenu[0].get_couleur())
        print(paquet_2.contenu[0].get_nom() , paquet_2.contenu[0].get_couleur())
        if paquet_1.contenu[0].valeur > paquet_2.contenu[0].valeur : # si la valeur de la carte du paquet 1 est plus grande que la carte du paquet 2 alors suprimer la carte de la main et ajouter la carte aux paquet 1
            paquet_1.contenu.append(paquet_2.contenu[0])
            paquet_1.contenu.append(paquet_1.contenu[0])
            del(paquet_1.contenu[0])
            del(paquet_2.contenu[0])
            #carte.image()
        elif paquet_1.contenu[0].valeur == paquet_2.contenu[0].valeur :          # si la valeur de la carte des deux paquets est égale
            if len(paquet_1.contenu) < 3 or len(paquet_2.contenu) < 3 :        # Arreter le jeu lorsque qu'il reste deux cartes dans l'un des paquets
                print("partie terminer")
                break
                #carte.image()
            else:
                print("-------------------------main posé N°2-------------------------")
                print(paquet_1.contenu[2].get_nom() , paquet_1.contenu[2].get_couleur())
                print(paquet_2.contenu[2].get_nom() , paquet_2.contenu[2].get_couleur())
                if paquet_1.contenu[2].valeur > paquet_2.contenu[2].valeur:          # tirer la troisième cartes pour les départager
                    for i in range(3):
                        paquet_1.contenu.append(paquet_2.contenu[0])
                        paquet_1.contenu.append(paquet_1.contenu[0])
                        del(paquet_2.contenu[0])
                        del(paquet_1.contenu[0])
                        #carte.image()
                elif paquet_1.contenu[2].valeur == paquet_2.contenu[2].valeur :
                    if len(paquet_1.contenu) < 5 or len(paquet_2.contenu) < 5 :        # Arreter le jeu lorsque qu'il reste deux cartes dans l'un des paquets
                        print("partie terminer")
                        break
                    else:
                        print("-------------------------main posé N°3-------------------------")
                        print(paquet_1.contenu[4].get_nom() , paquet_1.contenu[4].get_couleur())
                        print(paquet_2.contenu[4].get_nom() , paquet_2.contenu[4].get_couleur())
                        if paquet_1.contenu[4].valeur > paquet_2.contenu[4].valeur:          # tirer la troisième cartes pour les départager
                            for i in range(6):
                                paquet_1.contenu.append(paquet_2.contenu[0])
                                paquet_1.contenu.append(paquet_1.contenu[0])
                                del(paquet_2.contenu[0])
                                del(paquet_1.contenu[0])
                                #carte.image()
                        else:
                            for i in range(6):
                                paquet_2.contenu.append(paquet_1.contenu[0])
                                paquet_2.contenu.append(paquet_2.contenu[0])
                                del(paquet_2.contenu[0])
                                del(paquet_1.contenu[0])
                                #carte.image()
                else:
                    for i in range(3):
                        paquet_2.contenu.append(paquet_1.contenu[0])
                        paquet_2.contenu.append(paquet_2.contenu[0])
                        del(paquet_2.contenu[0])
                        del(paquet_1.contenu[0])
                        #carte.image() 
        else:
            paquet_2.contenu.append(paquet_1.contenu[0])
            paquet_2.contenu.append(paquet_2.contenu[0])
            del(paquet_2.contenu[0])
            del(paquet_1.contenu[0])
            #carte.image()
        nombre_carte()
        print("tour : " , conteur)
        conteur += 1
        if len(paquet_1.contenu) == 0 or len(paquet_2.contenu) == 0 :
            print("partie terminer")
            break
            

def comparer_carte():
        """ Renvoie la carte la plus forte"""
        #paquet 1 superieur
        if paquet_1.contenu[0].valeur > paquet_2.contenu[0].valeur :
            print("La carte du paquet_1 est supérieur à la carte du paquet_2")
        #les 2 paquets égaux
        elif paquet_1.contenu[0].valeur == paquet_2.contenu[0].valeur :
            print("La carte du paquet_1 est égale à la carte du paquet_2")
            # l'un des 2 paquets a une longeur inférieur a 2
            if len(paquet_1.contenu) <= 2 or len(paquet_2.contenu) <= 2 :
                if len(paquet_1.contenu) <= 2 :
                    print("nombre de carte du paquet 1 insuffisant")
                if len(paquet_2.contenu) <= 2 :
                    print("nombre de carte du paquet 2 insuffisant")
            else:
                #paquet 1 superieur carte 3
                if paquet_1.contenu[2].valeur > paquet_2.contenu[2].valeur :
                    print("La carte N°3 du paquet_1 est supérieur à la carte du paquet_2")
                #les 2 paquets égaux encore
                elif paquet_1.contenu[2].valeur == paquet_2.contenu[2].valeur :
                    print("La carte N°5 du paquet_1 est égale à la carte du paquet_2")
                    if  len(paquet_1.contenu) <= 4 :
                        print("nombre de carte du paquet 1 insuffisant")
                    if  len(paquet_2.contenu) <= 4 :
                        print("nombre de carte du paquet 2 insuffisant")
                    #paquet 1 superieur carte 5
                    if paquet_1.contenu[2].valeur > paquet_2.contenu[2].valeur :
                        print("La carte N°5 du paquet_1 est supérieur à la carte du paquet_2")
                    #paquet 2 superieur carte 5
                    else:
                        print("La carte N°5 du paquet_1 est inférieur à la carte du paquet_2")
                #paquet 2 superieur carte 3
                else:
                    print("La carte N°3 du paquet_1 est inférieur à la carte du paquet_2")
        #paquet 2 superieur
        else:
            print("La carte du paquet_1 est inférieur à la carte du paquet_2")


def nombre_carte():
    """ permet de calculer le nombre de carte"""
    print("paquet_1 nombre de carte :" , len(paquet_1.contenu))
    print("paquet_2 nombre de carte :" , len(paquet_2.contenu))
    

input("AVERTISSEMENT !! SI VOUS N'AVEZ PAS LES CARTES DANS LE MEME DOSSIER QUE LE PROGRAMME , IL RISQUE DE NE PAS FONCTIONNER CORRECTEMENT. APPUYER SUR ENTRER SI TOUT EST OK")
carte = Carte(1 , 1)
paquet_52 = PaquetDeCarte()
paquet_1 = PaquetDeCarte()
paquet_2 = PaquetDeCarte()
paquet_52.remplir()
paquet_52.melanger_carte()
paquet_1.distribuer_carte()
affrontement()
print("-------------------------paquet_1-------------------------")
paquet_1.afficher_carte1()
print("-------------------------paquet_2-------------------------")
paquet_2.afficher_carte2()
