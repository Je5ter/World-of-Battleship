from game.bato import *
import random

class Entite():
    def __init__(self,nomJoueur):
        self.nom = nomJoueur
        self.tabTirs = [[0]*10 for i in range(10)]
        self.tirX = 0
        self.tirY = 0
        self.coule = False

    def reset(self):
        if self.type == 'Joueur':
            self.__init__(self.nom)
        else:
            self.__init__()

    def Tir(self,x,y,adversaire):
        for i in range(5):
            if (x,y) in adversaire.Bateaux.pos[i]:
                adversaire.Bateaux.pos[i].remove((x,y))
                if not (x,y) == (0,0):
                    adversaire.Bateaux.pos[i].append((-x,-y))
                else:
                    adversaire.Bateaux.pos[i].append((-10,-10))
                self.tabTirs[x][y] = 'T'
                for pos in adversaire.Bateaux.pos[i]:
                    (x,y) = pos
                    if x>=0 and y>=0:
                        return 'Touche'
                self.coule = True
                return 'Coule'
        if not (-x,-y) in adversaire.Bateaux.pos[i]:
            self.tabTirs[x][y] = 'M'
            return 'Miss'

    def afficherTirs(self):
        tab = [[0]*10 for i in range(10)]

        for i in range(10):
            txt = ''
            for j in range(10):
                if self.tabTirs[i][j] == 'M':
                    txt += 'O '
                elif self.tabTirs[i][j] == 'T':
                    txt += 'X '
                else:
                    txt += '~ '
            print(str(txt))
        print('\n')

    def chooseMax(self):
        max = -1
        pos = []
        for i in range(10):
            for j in range(10):
                if self.tabProba[i][j]>max:
                    max = self.tabProba[i][j]
                    pos = []
                if self.tabProba[i][j]==max:
                    pos.append((i,j))
        if len(pos) == 1:
            return pos[0]
        while 1 == 1:
            r = random.randint(0,len(pos)-1)
            (x,y) = pos[r]
            for (x0,y0) in self.Touche:
                dx = abs(x0 - x)
                dy = abs(y0 - y)
                if dx+dy == 1:
                    return pos[r]

    def probTot(self):
        nb = 0
        for i in range(10):
            for j in range(10):
                if self.tabProba[i][j] > 0:
                    nb +=  self.tabProba[i][j]
        return nb

    def Proba(self,a):
        if self.modeChasse:
            self.probaChasse()
        else:
            self.probaCherche()
        if a:
            self.afficherProba()

    def reinitProba(self):
        for x in range(10):
            for y in range(10):
                if self.tabProba[x][y] >= 0:
                    self.tabProba[x][y] = 0

    def probaChasse(self):
        self.reinitProba()
        for t in self.Rest:
            for o in ['N','S','E','O']:
                for pos in self.Touche:
                    for l in range(t):
                        for i in range(3):
                            for j in range(3):
                                self.ProbaBateauC(pos[0]+l*(i-1),pos[1]+l*(j-1),o,t)

    def ProbaBateauC(self,x,y,o,t):
        (dx,dy) = self.Bateaux.transpose(o)
        positions = []
        for i in range(t):
            if y+i*dy < 0 or y+i*dy > 9 or x+i*dx < 0 or x+i*dx > 9 or self.tabProba[x+i*dx][y+i*dy] == -1:
                return False
            else:
                positions.append((x+i*dx,y+i*dy))

        for pos in self.Touche:
            if not pos in positions:
                return False

        for i in range(t):
            if self.tabProba[x+i*dx][y+i*dy] >= 0:
                self.tabProba[x+i*dx][y+i*dy] += 1

    def ProbaBateau(self,x,y,o,t):
        (dx,dy) = self.Bateaux.transpose(o)
        for i in range(t):
            if y+i*dy < 0 or y+i*dy > 9 or x+i*dx < 0 or x+i*dx > 9 or self.tabProba[x+i*dx][y+i*dy] == -1:
                return False

        for i in range(t):
            if not self.tabProba[x+i*dx][y+i*dy] < 0 :
                self.tabProba[x+i*dx][y+i*dy] += 1

    def TirIA(self,x,y,adversaire):
        for i in range(5):
            if (x,y) in adversaire.Bateaux.pos[i]:
                adversaire.Bateaux.pos[i].remove((x,y))
                if not (x,y) == (0,0):
                    adversaire.Bateaux.pos[i].append((-x,-y))
                else:
                    adversaire.Bateaux.pos[i].append((-10,-10))
                self.tabTirs[x][y] = 'T'
                self.tabProba[x][y] = -2
                self.modeChasse = True
                self.Touche.append((x,y))
                for pos in adversaire.Bateaux.pos[i]:
                    (xi,yi) = pos
                    if xi>=0 and yi>=0:
                        return 'Touche'
                self.modeChasse = False
                if self.nom == 'BotQuad':
                    self.CouleQ()
                else:
                    self.Coule()
                return 'Coule'
        if not (-x,-y) in adversaire.Bateaux.pos[i]:
            self.tabTirs[x][y] = 'M'
            self.tabProba[x][y] = -1
            return 'Miss'

    def Coule(self):
        for pos in self.Touche:
            self.tabProba[pos[0]][pos[1]] = -1
            if pos[0]+1 <=9:
                self.tabProba[pos[0]+1][pos[1]] = -1
            if pos[0]-1 > 0:
                self.tabProba[pos[0]-1][pos[1]] = -1
            if pos[1]+1 <=9:
                self.tabProba[pos[0]][pos[1]+1] = -1
            if pos[1]-1 > 0:
                self.tabProba[pos[0]][pos[1]-1] = -1
        self.Rest.remove(len(self.Touche))
        self.Touche = []

    def afficherProba(self):

        for i in range(10):
            txt = ''
            for j in range(10):
                txt += str(self.tabProba[i][j])+'  '
            print (txt)
        print('\n')


class Joueur(Entite):
    def __init__(self,nomjoueur):
        super().__init__(nomjoueur)
        self.type = 'Joueur'
        self.Bateaux = BateauJ()

    def Visee(self,adversaire,a):
        x = self.tirX
        y = self.tirY
        print(self.Tir(x,y,adversaire))
        self.afficherTirs()

class JoueurIARandom(Entite):
    def __init__(self):
        super().__init__('BotRandom')
        self.Bateaux = BateauIA()
        self.type = 'Bot'

    def Visee(self,adversaire,a):
        self.tirX = random.randint (0,9)
        self.tirY = random.randint (0,9)
        while not self.tabTirs[self.tirX][self.tirY] == 0:
            self.tirX = random.randint (0,9)
            self.tirY = random.randint (0,9)
        if a:
            print(self.Tir(self.tirX,self.tirY,adversaire))
        else:
            self.Tir(self.tirX,self.tirY,adversaire)

class JoueurIADecroissant(Entite):
    '''def choose(self,proba,x,y):
        tab = [(-1,-1)]*100
        for i in range(int(proba*100)):
            tab[i] = (x,y)
        return tab[random.randint(0,99)]'''
    def choose(self,proba,x,y):
        tab = [(-1,-1)]*100
        for i in range(int(proba*100)):
            tab[i] = (x,y)
        ok = False
        while (ok == False):
            a = random.randint(0,99)
            if ((tab[a][0])%2 == 0 and (tab[a][1])%2 == 0) or ((tab[a][0])%2 == 1 and (tab[a][1])%2 == 1):
                ok = True
        return tab[a]

    def __init__(self):
        super().__init__('BotDecroi')
        self.Bateaux = BateauIA()
        self.tabProba = [[0]*10 for i in range(10)]
        self.modeChasse = False
        self.Touche = []
        self.type = 'Bot'
        self.Rest = [2,3,3,4,5]
        self.Proba(False)

    def Visee(self,adversaire,a):
        self.Proba(a)
        (self.tirX,self.tirY) = (-1,-1)
        Max = self.probTot()
        while (self.tirX,self.tirY) ==(-1,-1):
            i = random.randint(0,9)
            j = random.randint(0,9)
            if self.tabProba[i][j] > 0 and (self.tirX,self.tirY) == (-1,-1):
                if self.modeChasse:
                    (self.tirX,self.tirY) = self.chooseMax()
                else:
                    (self.tirX,self.tirY) = self.choose(self.tabProba[i][j]/Max,i,j)
        self.TirIA(self.tirX,self.tirY,adversaire)

    def probaCherche(self):
        self.reinitProba()
        for x in range(10):
            for y in range(10):
                for o in ['S','E']:
                    t = self.Rest[len(self.Rest)-1]
                    self.ProbaBateau(x,y,o,t)

class JoueurIAProba(Entite):
    def choose(self,proba,x,y):
        tab = [(-1,-1)]*100
        for i in range(int(proba*100)):
            tab[i] = (x,y)
        return tab[random.randint(0,99)]

    def __init__(self):
        super().__init__('BotProba')
        self.Bateaux = BateauIA()
        self.type = 'Bot'
        self.tabProba = [[0]*10 for i in range(10)]
        self.modeChasse = False
        self.Touche = []
        self.Rest = [2,3,3,4,5]
        self.Proba(False)

    def Visee(self,adversaire,a):
        self.Proba(a)
        (self.tirX,self.tirY) = (-1,-1)
        Max = self.probTot()
        while (self.tirX,self.tirY) ==(-1,-1):
            i = random.randint(0,9)
            j = random.randint(0,9)
            if self.tabProba[i][j] > 0 and (self.tirX,self.tirY) == (-1,-1):
                if self.modeChasse:
                    (self.tirX,self.tirY) = self.chooseMax()
                else:
                    (self.tirX,self.tirY) = self.choose(self.tabProba[i][j]/Max,i,j)
        self.TirIA(self.tirX,self.tirY,adversaire)

    def probaCherche(self):
        self.reinitProba()
        for x in range(10):
            for y in range(10):
                for o in ['S','E']:
                    for t in self.Rest:
                        self.ProbaBateau(x,y,o,t)

class JoueurIADia (Entite):
    def choose(self,proba,x,y):
        tab = [(-1,-1)]*100
        for i in range(int(proba*100)):
            tab[i] = (x,y)
        ok = False
        while (ok == False):
            a = random.randint(0,99)
            if ((tab[a][0])%2 == 0 and (tab[a][1])%2 == 0) or ((tab[a][0])%2 == 1 and (tab[a][1])%2 == 1):
                ok = True
        return tab[a]

    def __init__(self):
        super().__init__('BotDia')
        self.Bateaux = BateauIA()
        self.type = 'Bot'
        self.tabProba = [[0]*10 for i in range(10)]
        self.modeChasse = False
        self.Touche = []
        self.Rest = [2,3,3,4,5]
        self.Proba(False)

    def Visee(self,adversaire,a):
        self.Proba(a)
        (self.tirX,self.tirY) = (-1,-1)
        Max = self.probTot()
        while (self.tirX,self.tirY) ==(-1,-1):
            i = random.randint(0,9)
            j = random.randint(0,9)
            if self.tabProba[i][j] > 0 and (self.tirX,self.tirY) == (-1,-1):
                if self.modeChasse:
                    (self.tirX,self.tirY) = self.chooseMax()
                else:
                    (self.tirX,self.tirY) = self.choose(self.tabProba[i][j]/Max,i,j)
        self.TirIA(self.tirX,self.tirY,adversaire)

    def probaCherche(self):
        self.reinitProba()
        for x in range(10):
            for y in range(10):
                for o in ['S','E']:
                    for t in self.Rest:
                        self.ProbaBateau(x,y,o,t)

class JoueurIAQua (Entite):
    def __init__(self):
        super().__init__('BotQua')
        self.Bateaux = BateauIA()
        self.type = 'Bot'
        self.tabProba = [[0]*10 for i in range(10)]
        self.modeChasse = False
        self.Touche = []
        self.Rest = [2,3,3,4,5]
        self.Proba(False)

    def chooseQ(self):
        tab = self.tabp()
        vide = True
        for i in range(10):
            for j in range(10):
                if self.tabTirs[i][j] == 'M' or self.tabTirs[i][j] == 'T':
                    vide = False
        if vide:
            return (random.randint(0,9),random.randint(0,9))
        ok = False
        while not ok:
            a = random.randint(0,len(tab)-1)
            cx = tab[a][0]
            cy = tab[a][1]
            if cx+1<10 and cy+1<10:
                if self.tabProba[cx+1][cy+1] == -1:
                    ok = True
            if cx+1<10 and cy-1>=0:
                if self.tabProba[cx+1][cy-1] == -1:
                    ok = True
            if cx-1>=0 and cy+1<10:
                if self.tabProba[cx-1][cy+1] == -1:
                    ok = True
            if cx-1>=0 and cy-1>=0:
                if self.tabProba[cx-1][cy-1] == -1:
                    ok = True
        return tab[a]

    def tabp(self):
        tab = []
        for i in range(10):
            for j in range(10):
                Max = self.probTot()
                for k in range(int(1000*self.tabProba[i][j]/Max)):
                    tab.append((i,j))
        return (tab)

    #fonction appelée dans tour pour choisir la case ciblée : par probabilitées
    def Visee(self,adversaire,a):
        self.Proba(a)
        (self.tirX,self.tirY) = (-1,-1)
        Max = self.probTot()
        while (self.tirX,self.tirY) ==(-1,-1):
            i = random.randint(0,9)
            j = random.randint(0,9)
            if self.tabProba[i][j] > 0 and (self.tirX,self.tirY) == (-1,-1):
                if self.modeChasse:
                    (self.tirX,self.tirY) = self.chooseMax()
                else:
                    self.tabp()
                    (self.tirX,self.tirY) = self.chooseQ()
        self.TirIA(self.tirX,self.tirY,adversaire)

    def probaCherche(self):
        self.reinitProba()
        for x in range(10):
            for y in range(10):
                for o in ['S','E']:
                    for t in self.Rest:
                        self.ProbaBateau(x,y,o,t)

class JoueurIACinq (Entite):
    def __init__(self):
        super().__init__('BotCinq')
        self.Bateaux = BateauIA()
        self.type = 'Bot'
        self.tabProba = [[0]*10 for i in range(10)]
        self.modeChasse = False
        self.Touche = []
        self.Rest = [2,3,3,4,5]
        self.Proba(False)

    def chooseQ(self):
        maxi = self.tabp()
        a = random.randint(0, 4)
        return maxi[a]

    def tabp(self):
        maxi = [(0,0), (0,0), (0,0), (0,0), (0,0)]
        for i in range(10):
            for j in range(10):
                valid = True
                if (self.tabProba[i][j] >= self.tabProba[maxi[0][0]][maxi[0][1]]):
                    maxi[4] = maxi[3]
                    maxi[3] = maxi[2]
                    maxi[2] = maxi[1]
                    maxi[1] = maxi[0]
                    maxi[0] = (i, j)
                    valid = False
                if valid and (self.tabProba[i][j] >= self.tabProba[maxi[1][0]][maxi[1][1]]):
                    maxi[4] = maxi[3]
                    maxi[3] = maxi[2]
                    maxi[2] = maxi[1]
                    maxi[1] = (i, j)
                    valid = False
                if valid and (self.tabProba[i][j] >= self.tabProba[maxi[2][0]][maxi[2][1]]):
                    maxi[4] = maxi[3]
                    maxi[3] = maxi[2]
                    maxi[2] = (i, j)
                    valid = False
                if valid and (self.tabProba[i][j] >= self.tabProba[maxi[3][0]][maxi[3][1]]):
                    maxi[4] = maxi[3]
                    maxi[3] = (i, j)
                    valid = False
                if valid and (self.tabProba[i][j] >= self.tabProba[maxi[4][0]][maxi[4][1]]):
                    maxi[4] = (i, j)
                    valid = False
        return (maxi)


    #fonction appelée dans tour pour choisir la case ciblée : par probabilitées
    def Visee(self,adversaire,a):
        self.Proba(a)
        (self.tirX,self.tirY) = (-1,-1)
        Max = self.probTot()
        while (self.tirX,self.tirY) ==(-1,-1):
            i = random.randint(0,9)
            j = random.randint(0,9)
            if self.tabProba[i][j] > 0 and (self.tirX,self.tirY) == (-1,-1):
                if self.modeChasse:
                    (self.tirX,self.tirY) = self.chooseMax()
                else:
                    self.tabp()
                    (self.tirX,self.tirY) = self.chooseQ()
        self.TirIA(self.tirX,self.tirY,adversaire)

    def probaCherche(self):
        self.reinitProba()
        for x in range(10):
            for y in range(10):
                for o in ['S','E']:
                    for t in self.Rest:
                        self.ProbaBateau(x,y,o,t)

class JoueurIACroissant(Entite):
    def choose(self,proba,x,y):
        tab = [(-1,-1)]*100
        for i in range(int(proba*100)):
            tab[i] = (x,y)
        return tab[random.randint(0,99)]

    def __init__(self):
        super().__init__('BotCroi')
        self.Bateaux = BateauIA()
        self.tabProba = [[0]*10 for i in range(10)]
        self.modeChasse = False
        self.Touche = []
        self.type = 'Bot'
        self.Rest = [2,3,3,4,5]
        self.Proba(False)

    def Visee(self,adversaire,a):
        self.Proba(a)
        (self.tirX,self.tirY) = (-1,-1)
        Max = self.probTot()
        while (self.tirX,self.tirY) ==(-1,-1):
            i = random.randint(0,9)
            j = random.randint(0,9)
            if self.tabProba[i][j] > 0 and (self.tirX,self.tirY) == (-1,-1):
                if self.modeChasse:
                    (self.tirX,self.tirY) = self.chooseMax()
                else:
                    (self.tirX,self.tirY) = self.choose(self.tabProba[i][j]/Max,i,j)
        self.TirIA(self.tirX,self.tirY,adversaire)

    def probaCherche(self):
        self.reinitProba()
        for x in range(10):
            for y in range(10):
                for o in ['S','E']:
                    t = self.Rest[0]
                    self.ProbaBateau(x,y,o,t)


class JoueurIAQuadrillage(Entite):
    def choose(self,proba,x,y):
        tab = [(-1,-1)]*100
        for i in range(int(proba*100)):
            tab[i] = (x,y)
        return tab[random.randint(0,99)]

    def __init__(self):
        super().__init__('BotQuad')
        self.Bateaux = BateauIA()
        self.tabProba = [[0]*10 for i in range(10)]
        self.modeChasse = False
        self.Touche = []
        self.type = 'Bot'
        self.Rest = [2,3,3,4,5]
        self.Proba(False)
        self.carres = [[0,0],[0,5],[5,0],[5,5]]
        self.probaCarres = [0,0,0,0]
        self.CarreActu = self.carres[random.randint(0,3)]

    def Visee(self,adversaire,a):
        self.Proba(a)
        (self.tirX,self.tirY) = (-1,-1)
        Max = self.probTot()
        while (self.tirX,self.tirY) ==(-1,-1):
            if self.modeChasse:
                (self.tirX,self.tirY) = self.chooseMax()
            else:
                self.choixCarre()
                for i in range(5):
                    for j in range(5):
                        if self.tabProba[i+self.CarreActu[0]][j+self.CarreActu[1]] > 0 and (self.tirX,self.tirY) == (-1,-1):
                            (self.tirX,self.tirY) = self.choose(self.tabProba[i+self.CarreActu[0]][j+self.CarreActu[1]]/Max,i,j)
        self.TirIA(self.tirX,self.tirY,adversaire)

    def probaCherche(self):
        self.reinitProba()
        for x in range(10):
            for y in range(10):
                for o in ['S','E']:
                    for t in self.Rest:
                        self.ProbaBateau(x,y,o,t)

    def CouleQ(self):
        self.Coule()
        self.modeChasse = False
        self.choixCarre()

    def choixCarre(self):
        self.reinitProba()
        self.Proba(False)
        self.actuProbCarre()
        maxi = -1
        n = -1
        for i in range(4):
            if self.probaCarres[i]>maxi:
                maxi =self.probaCarres[i]
                n = i
        self.CarreActu = self.carres[n]
        print (str(self.CarreActu))

    def actuProbCarre(self):
        somme = 0
        liste = [0,0,0,0]
        for dx in (0,5):
            for dy in (0,5):
                for i in range(5):
                    for j in range(5):
                        if self.tabProba[i+dx][j+dy] > 0:
                            somme += self.tabProba[i+dx][j+dy]
                liste[int(dy/5+2*dx/5)] = somme
        self.probaCarres = liste
        print (str(somme))
