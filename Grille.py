import tkinter as tk
import random as rd

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

def affichage(Grille):
    a = mélangerlignes(Grille)
    b = mélangercolonnes(a)
    c = cryptage(b)

    for n in range(len(c)):
        for t in range(len(c)):
            position = grille.create_text((Taille-565)+(t*(Taille-533)), (Taille-570)+(n*(Taille-533)), text= str(c[n][t]), font="35")

lancement = tk.Button(fenetre, command= lambda : affichage(G1), text= "On commence ?")
lancement.grid(row= 0, column= 1)

fenetre.mainloop()