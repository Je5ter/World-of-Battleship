from game.joueur import *
import random


class Partie:
    def __init__(self, j1, j2):
        self.joueurs = [j1, j2]
        self.type = [0, 0]
        self.current = 0
        self.opponent = 1
        self.winner = [False, 0]
        self.nbTours = 0
    
    def Tour(self, affichage, nb):
        if not self.winner[0]:
            if affichage:
                print('Joueur' + str(self.current + 1) + ' : ' + self.joueurs[self.current].nom)
                print('Etat de la flotte : \n')
                self.joueurs[self.current].Bateaux.afficher()
                print('Tableau de Tirs : \n')
                self.joueurs[self.current].afficherTirs()
            self.joueurs[self.current].Visee(self.joueurs[self.opponent], affichage)
            self.checkWin(self.joueurs[self.opponent].Bateaux.pos)
            if self.current == 0:
                self.current = 1
                self.opponent = 0
            else:
                self.current = 0
                self.opponent = 1
                self.nbTours += 1
            if nb != 1:
                return self.Tour(affichage, nb)
        else:
            if affichage:
                print('Winner Joueur' + str(self.winner[1] + 1) + ' : ' + self.joueurs[self.winner[1]].nom)
                print('nombre de coups : ' + str(self.nbTours))
            result = [self.joueurs[self.winner[1]].nom, self.nbTours]
            return result
    
    def checkWin(self, positions):
        for i in range(5):
            for pos in positions[i]:
                (x, y) = pos
                if x > 0 or y > 0 or (x == 0 and y == 0):
                    return False
        self.winner = [True, self.current]


class PartiePredef:
    def __init__(self):
        self.Parties = []
        self.result = []
        self.joueur1 = None
        self.joueur2 = None
        self.nb = 1
        self.nomJ = ''
    
    def Start(self):
        if self.nb != 1:
            for i in range(self.nb):
                self.joueur1.reset()
                self.joueur2.reset()
                self.Parties.append(Partie(self.joueur1, self.joueur2))
                self.result.append(self.Parties[i].Tour(False, self.nb))
            
            # if self.nb == 1:
            #     return(self.result)
            # else:
            print("résultat = " + str(self.result))
            self.Stats(self.result)
    
    def inputJoueur(self, j):
        # j = str(input('Choisissez le type du joueur'+str(nombre)+' (J , IAProba , IARandom , IADecroi , IACroi , IAQuad, IACinq) : '))
        if j == 'J':
            return Joueur(self.nomJ)
        if j == 'IAProba':
            return JoueurIAProba()
        if j == 'IARandom':
            return JoueurIARandom()
        if j == 'IADecroi':
            return JoueurIADecroissant()
        if j == 'IACroi':
            return JoueurIACroissant()
        if j == 'IAQua':
            return JoueurIAQua()
        if j == 'IADia':
            return JoueurIADia()
        if j == 'IACinq':
            return JoueurIACinq()
        return self.inputJoueur()
    
    def Stats(self, tab):
        self.J1 = [tab[0][0], 0, []]
        if self.Parties[0].joueurs[0].nom == tab[0][0]:
            self.J2 = [self.Parties[0].joueurs[1].nom, 0, []]
        else:
            self.J2 = [self.Parties[0].joueurs[0].nom, 0, []]
        for i in range(len(tab)):
            if tab[i][0] == self.J1[0]:
                self.J1[1] += 1 / self.nb
                self.J1[2].append(tab[i][1])
            
            else:
                self.J2[0] = tab[i][0]
                self.J2[1] += 1 / self.nb
                self.J2[2].append(tab[i][1])
        
        self.J1[2] = self.moyenne(self.J1[2])
        self.J2[2] = self.moyenne(self.J2[2])
        
        print('le joueur : ' + self.J1[0] + ' a gagné ' + str(self.J1[1] * 100) + '% du temps')
        print('Son nombre de coups gagnants moyen est : ' + str(self.J1[2]))
        print('Avec un max de : ' + str(self.minmax(self.J1[0])[0]) + ' et un min de : ' + str(
            self.minmax(self.J1[0])[1]))
        print('le joueur : ' + self.J2[0] + ' a gagné ' + str(self.J2[1] * 100) + '% du temps')
        print('Son nombre de coups gagnants moyen est : ' + str(self.J2[2]))
        print('Avec un max de : ' + str(self.minmax(self.J2[0])[0]) + ' et un min de : ' + str(
            self.minmax(self.J2[0])[1]))
        # R = str(input('Rejouer avec les mêmes parametres ? (Y/N) '))
        # print('\n')
        # if R == 'Y':
        #     self.Parties = []
        #     self.result = []
        #     self.Start()
    
    def moyenne(self, tab):
        S = 0
        if not tab == []:
            for i in range(len(tab)):
                S += int(tab[i])
            
            return S / len(tab)
        else:
            return 0
    
    def valeurs(self, nomJ):
        tab = []
        for i in range(len(self.result)):
            if self.result[i][0] == nomJ:
                tab.append(self.result[i][1])
        
        return tab
    
    def minmax(self, nomJ):
        maxi = -1
        mini = 99999
        for i in range(len(self.result)):
            if self.result[i][0] == nomJ:
                maxi = max(maxi, self.result[i][1])
                mini = min(mini, self.result[i][1])
        
        return [maxi, mini]


partie = PartiePredef()
