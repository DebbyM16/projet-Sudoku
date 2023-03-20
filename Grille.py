import tkinter as tk
import random as rd

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

#Cette fonction sert à mélanger les colonnes dans une même rangée de 3

def mélangercolonnes(G):
    L = [[], [], [], [], [], [], [], [], []]
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

    
#Cette fonction sert à crypter une grille grâce à une clé de cryptage prise au hasard 

def cryptage(G):
    L = []
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

# Bouton pour commencer la partie

def affichage(G):
    a = mélangerlignes(G)
    b = mélangercolonnes(a)
    c = cryptage(b)

    for n in range(len(c)):
        for t in range(len(c)):
            position = grille.create_text((Taille-565)+(t*(Taille-533)), (Taille-570)+(n*(Taille-533)), text= str(c[n][t]), font="35")

lancement = tk.Button(fenetre, command= lambda : affichage(G1), text= "On commence ?")
lancement.grid(row= 0, column= 1)

fenetre.mainloop()