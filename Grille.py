import tkinter as tk

G1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9] ,  
      [7, 8, 9, 1, 2, 3, 4, 5, 6] , 
      [4, 5, 6, 7, 8, 9, 1, 2, 3] , 
      [9, 1, 2, 3, 4, 5, 6, 7, 8] , 
      [6, 7, 8, 9, 1, 2, 3, 4, 5] , 
      [3, 4, 5, 6, 7, 8, 9, 1, 2] , 
      [8, 9, 1, 2, 3, 4, 5, 6, 7] , 
      [5, 6, 7, 8, 9, 1, 2, 3, 4] , 
      [2, 3, 4, 5, 6, 7, 8, 9, 1]]



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

# Création de la fenêtre

Taille = 600
Case = 9

fenetre = tk.Tk()
fenetre.title("Sudoku")

grille = tk.Canvas(height= Taille, width= Taille)
grille.grid()

# Création de la grille

for i in range(Case+1):
    if i % 3 == 0:
        verticale = grille.create_line((i*Taille)/Case, 0, (i*Taille)/Case, Taille, width= 3)
        horizontale = grille.create_line(0,(i*Taille)/Case, Taille, (i*Taille)/Case, width= 3)
    else:
        verticale = grille.create_line((i*Taille)/Case, 0, (i*Taille)/Case, Taille)
        horizontale = grille.create_line(0,(i*Taille)/Case, Taille, (i*Taille)/Case)

def affichage(G):
    a = mélangerlignes(G)
    b = mélangercolonnes(a)
    c = cryptage(b)

    for n in range(Case+1):
        for t in range(Case+1):
            position = grille.create_text()

# Bouton pour commencer la partie

lancement = tk.Button(fenetre, text= "On commence ?", command= affichage(G1))
lancement.grid(row= 0, column= 1)

fenetre.mainloop()