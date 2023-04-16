G1 = [[9, 1, 4, 5, 2, 3, 8, 7, 6] ,  
      [3, 7, 5, 9, 0, 0, 4, 2, 1] , 
      [0, 2, 8, 0, 1, 0, 3, 5, 9] , 
      [2, 9, 6, 4, 5, 1, 7, 8, 0] , 
      [5, 8, 3, 0, 7, 0, 9, 1, 4] , 
      [1, 0, 7, 8, 0, 9, 0, 6, 2] , 
      [4, 6, 9, 0, 8, 0, 2, 3, 5] , 
      [0, 3, 1, 2, 0, 0, 6, 9, 8] , 
      [8, 0, 2, 3, 0, 6, 1, 4, 7]]


[[9, 1, 4, 5, 2, 3, 8, 7, 6], 
 [3, 7, 5, 9, 6, 8, 4, 2, 1], 
 [6, 2, 8, 7, 1, 4, 3, 5, 9], 
 [2, 9, 6, 4, 5, 1, 7, 8, 3], 
 [5, 8, 3, 6, 7, 2, 9, 1, 4], 
 [1, 4, 7, 8, 3, 9, 5, 6, 2], 
 [4, 6, 9, 1, 8, 7, 2, 3, 5], 
 [7, 3, 1, 2, 4, 5, 6, 9, 8],
 [8, 5, 2, 3, 9, 6, 1, 4, 7]]

import random as rd

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
    


def sum(G) :
    n = 0
    for i in range(0, 9) :
        for j in range(0, 9) :
            n += G[i][j]
    return n



def countnumb(L) :
    n = 0
    for i in range(1, 10) :
        if L.count(i) <= 1 or L[i - 1] == 0 :
            n += 1
    return n == 9



def listcolumn(G, n) :
    L = []
    for i in range(0, 9) :
        L.append(G[i][n])
    return L



def errorbloc(G, n) :
    L = []
    a = n % 3
    b = n - a
    for i in range(b, b + 3) :
        for j in range(a * 3, a * 3 + 3) :
            L.append(G[i][j])
    if countnumb(L) :
        return True



def error(G) :
    n = 0
    for i in range(0, 9) :
        if countnumb(G[i]) :
            n += 1
    for j in range(0, 9) :
        if countnumb(listcolumn(G, j)):
            n += 1
    for k in range(0, 9) :
        if errorbloc(G, k) :
            n += 1
    return n == 27



def epure(L) :
    while 0 in L :
        L.remove(0)
    return L



def verify(G) :
    for l in range(0, 8) :
        L = []
        n = 0
        for i in range(0, 9) :
            if G[l][i] == 0 :
                n += 1
                for j in range(1, 10) :
                    G[l][i] = j
                    if error(G) :
                         L.append(j)
                         G[l][i] = 0
                    else :
                         G[l][i] = 0
                    L.append(0)
        if len(epure(L)) == n and n != 0 :
            o = 0
            for k in range(0, 9) :
                if G[l][k] == 0 :
                    G[l][k] = L[o]
                    o += 1

    return G




#Partie aide

# Cette fonction remplis une case choisie automatiquement 

def aide():
    global nouvelle_grille, X, Y, message_erreur, hasard, end
    pressNum(nouvelle_grille[X][Y])
    message_erreur.set('')
    if hasard == []:
        end = False
        finish = tk.Label(fenetre, relief= "groove", fg = 'red', text= "BRAVO ! Vous avez gagné !")
        finish.grid(row=0, column=0, columnspan=10)


btn_aide["state"] = "normal"

# Bouton d'aide 

btn_aide = tk.Button(fenetre, text="Aide", font=("helvetica", 15), fg=("red"), bd=0.5, command=lambda:aide(), state= "disable")
btn_aide.grid(row=1, column= 10)







