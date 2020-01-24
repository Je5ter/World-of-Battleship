import random

class Bateaux:

    def __init__(self):
        self.pos = [[]for i in range(5)]

    def placement(self,x,y,o,t):
        (dx,dy) = self.transpose(o)
        positions = []
        if (dx,dy) == (0,0):
            return positions

        for i in range(t):
            for j in range(len(self.pos)):
                if y+i*dy < 0 or y+i*dy > 9 or x+i*dx< 0 or x+i*dx > 9:
                    return positions
                if ((x+i*dx+dy,y+i*dy+dx) in self.pos[j]) or ((x+i*dx-dy,y+i*dy-dx) in self.pos[j]):
                    return positions

        for i in range(t+2):
            for j in range(len(self.pos)):
                if (x+(i-1)*dx,y+(i-1)*dy) in self.pos[j]:
                    return positions

        for i in range(t):
            positions.append((x+i*dx,y+i*dy))

        return positions


    def transpose(self,o):
        if o == 'N':
            return (-1,0)
        elif o == 'S':
            return (1,0)
        elif o == 'E':
            return (0,1)
        elif o == 'O':
            return (0,-1)
        else:
            return (0,0)

    def afficher(self):
        tab = [[0]*10 for i in range(10)]
        for bato in self.pos:
            for pos in bato:
                (x,y) = pos
                if x>=0 and y>=0:
                    tab[x][y] = 'B'
                else:
                    if (x,y) == (-10,-10):
                        tab[0][0] = 'X'
                    else:
                        tab[-x][-y] = 'X'

        for i in range(10):
            txt = ''
            for j in range(10):
                if tab[i][j] == 'B':
                    txt += 'O '
                elif tab[i][j] == 'X':
                    txt += 'X '
                else:
                    txt += '~ '
            print(str(txt))

class BateauIA(Bateaux):

    def __init__(self):
        super().__init__()
        self.o = ['N','S','O','E']
        self.i = 0
        for Taille in [2,3,3,4,5]:
            while  self.pos[self.i] == []:
                x = random.randint (0,9)
                y = random.randint (0,9)
                o = self.o[random.randint(0,3)]
                self.pos[self.i] = Bateaux.placement(self,x,y,o,Taille)
            self.i += 1


class BateauJ(Bateaux):

    def __init__(self):
        super().__init__()


# def initManu():
#     BatoIa = BateauIA()
#     BatoIa.afficher()
