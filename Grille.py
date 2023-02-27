import tkinter as tk
import random

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

lancement = tk.Button(fenetre, text= "On commence ?")
lancement.grid(row= 0, column= 1)

fenetre.mainloop()