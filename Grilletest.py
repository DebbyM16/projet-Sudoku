G1 = [[9, 1, 4, 5, 2, 3, 8, 7, 6] ,  
      [3, 7, 5, 9, 6, 8, 4, 2, 1] , 
      [6, 2, 8, 7, 1, 4, 3, 5, 9] , 
      [2, 9, 6, 4, 5, 1, 7, 8, 3] , 
      [5, 8, 3, 6, 7, 2, 9, 1, 4] , 
      [1, 4, 7, 8, 3, 9, 5, 6, 2] , 
      [4, 6, 9, 1, 8, 7, 2, 3, 5] , 
      [7, 3, 1, 2, 4, 5, 6, 9, 8] , 
      [8, 5, 2, 3, 9, 6, 1, 4, 7]]



#Cette fonction sert à mélanger les lignes dans une même rangée de 3 

def mélangerlignes(G):
    L = []
    import random as rd
    for i in range(0, 3):
        a = rd.randint(0, 2)
        L.append(G[a])
        del G[a]
        a = rd.randint(0, 1)
        L.append(G[a])
        del G[a]
        L.append(G[0])
        del G[0]
    return L
    
#Cette fonction sert à crypter une grille grâce à une clé de cryptage prise au hasard 

def cryptage(G):
    L = []
    import random as rd
    while len(L) < 9 :
        a = rd.randint(1, 9)
        if a not in L :
            L.append(a)
    for i in range(0, 9):
        for j in range(0, 9):
            for n in range(0, 9):
                if G[i][j] == n + 1 :
                    G[i][j] = L[n]
                    break
            
    return G

#Cette fonction sert à mélanger les colonnes dans une même rangée de 3

def mélangercolonnes(G):
    L = [[], [], [], [], [], [], [], [], []]
    import random as rd
    for j in range(0, 3):
        n = rd.randint(0, 2)
        for i in range(0, 9):
            L[i].append(G[i][n])
            del G[i][n]
        n = rd.randint(0, 1)
        for i in range(0, 9):
            L[i].append(G[i][n])
            del G[i][n]
        for i in range(0, 9):
            L[i].append(G[i][0])
            del G[i][0]
    return L

#Cette fonction sert à donner le numéro du bloc en rentrant les coordonnées d'une case (ligne/colonne)

def numbloc(l, c):
    for j in range(0, 3):
        if 3 * j + 1 <= l <= (j + 1) * 3 :
            for i in range(0, 3):
                if i * 3 + 1 <= c <= (i + 1) * 3 :
                    num = 3 * j + i + 1
                    break
    return num

#no

def MélangerLignes(G):
    L = []
    L.append(G[0])
    import random as rd 
    while len(L) != 2 :
        n = 0
        a = rd.randint(1, 8)
        for i in range(1, 10):
            if numbloc(1, G[0].index(i) + 1) != numbloc(2, G[a].index(i) + 1):
                n = n + 1
            else :
                break
        if n == 9 :
            L.append(G[a])
            del G[a]
    return L




def crete() : 
    L = [[], [], [], [], [], [], [], [], []]
    import random as rd
    while len(L[0]) < 9 :
        a = rd.randint(1, 9)
        if a not in L[0] :
            L.append(a)
    while len(L) != 2 :
        n = 0
        while len(L[1]) < 9 :
            a = rd.randint(1, 9)
            if a not in L[1] :
                L.append(a)
        for i in range(1, 10):
            if numbloc(1, L[0].index(i) + 1) == numbloc(2, L[1].index(i) + 1):
                n = n + 1
        if n != 0 :
            del L[1]           
    return L

def create() :
    L = [[], [], [], [], [], [], [], [], []]
    import random as rd
    while len(L[0]) < 9 :
        a = rd.randint(1, 9)
        if a not in L[0] :
            L.append(a)
    







print(mélangercolonnes(mélangerlignes(cryptage(G1))))





A = [[4, 2, 8, 9, 6, 3, 5, 7, 1], 
     [1, 5, 7, 4, 8, 2, 3, 6, 9], 
     [9, 3, 6, 1, 7, 5, 2, 8, 4], 
     [2, 7, 4, 3, 9, 8, 6, 1, 5], 
     [5, 6, 1, 2, 4, 7, 8, 9, 3], 
     [3, 8, 9, 5, 1, 6, 7, 4, 2], 
     [8, 4, 3, 6, 5, 9, 1, 2, 7], 
     [6, 9, 5, 7, 2, 1, 4, 3, 8], 
     [7, 1, 2, 8, 3, 4, 9, 5, 6]
     ]