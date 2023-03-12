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

print(G1)


def mélangerlignes(G):
    import random as rd
    for i in range(1, 4):
        a = rd.randint(1, 3)
        G[i] = G[a]
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

lancement = tk.Button(fenetre, text= "On commence ?", command=)
lancement.grid(row= 0, column= 1)

fenetre.mainloop()