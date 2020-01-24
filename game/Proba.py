def ProbaStart():
    Proba = [[0]*10 for i in range(10)]
    Bato = [2,3,4,4,5]
    for i in range(10):
        for j in range(10):
            for t in Bato:
                Proba = ActuProba(Proba,i,j,'gauche',t)
                Proba = ActuProba(Proba,i,j,'bas',t)
    return Proba


def ActuProba(Proba,x,y,o,nb):
        if o == 'gauche':
            for i in range(nb):
                if y-i < 0 or y-i > 9 or x< 0 or x > 9 or Proba[x][y-i] == 'f':
                    return Proba

            for j in range(nb):
                Proba[x][y-j] += 1
            return Proba

        if o == 'bas':
            for i in range(nb):
                if y < 0 or y > 9 or x+i < 0 or x+i > 9 or Proba[x+i][y] == 'f' :
                    return Proba
            for j in range(nb):
                Proba[x+j][y] += 1
            return Proba
