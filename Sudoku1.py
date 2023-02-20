import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Sudoku")

grille = tk.Canvas(fenetre, height= 500, width= 500)
grille.grid()

for i in range(1, 10):
    for j in range(1, 10):
        grille.create_rectangle(((i-1)*(500//9), (j-1)*(500//9)),
                (i*(500//9),j*(500//9)), fill= "white")
        numero = tk.Label(text=str(j))
        numero.grid(column= (j-1)*(500//9), row= (i-1)*(500//9))

fenetre.mainloop() # Lancement de la boucle principale