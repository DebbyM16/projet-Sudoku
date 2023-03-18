import tkinter as tk

Taille = 600
Case = 9
fenetre = tk.Tk()
fenetre.title("Sudoku")
fenetre.geometry("700x700")

#écran d'affichage
result = tk.StringVar() 
result.set("0") #la valeur initiale = 0

#création de la grille
grille = tk.Canvas(height= Taille, width= Taille)
grille.grid()
for i in range(Case+1):
    if i % 3 == 0:
        verticale = grille.create_line((i*Taille)/Case, 0, (i*Taille)/Case, Taille, width=3)
        horizontale = grille.create_line(0, (i*Taille)/Case, Taille, (i*Taille)/Case, width=3)
    else:
        verticale = grille.create_line((i*Taille)/Case, 0, (i*Taille)/Case, Taille)
        horizontale = grille.create_line(0, (i*Taille)/Case, Taille, (i*Taille)/Case)

#affichage des chiffres qu'on a cliqué
affichage = tk.Label(grille, font=("helvetica", 30), bg="grey", bd="9", fg="black", anchor="se", textvariable=result) #lorsqu'on a changé les chiffres de l'écran, "result" vas prendre valeurs qu'on a changé
affichage.place(x=0, y=0, width=67, height=67)

#boutons des chiffres
bouton1 = tk.Button(fenetre, text="1", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum("1"))
bouton1.place(x=0, y=600, width=50, height=50)

bouton2 = tk.Button(fenetre, text="2", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum("2"))
bouton2.place(x=50, y=600, width=50, height=50)

bouton3 = tk.Button(fenetre, text="3", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum("3"))
bouton3.place(x=100, y=600, width=50, height=50)

bouton4 = tk.Button(fenetre, text="4", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum("4"))
bouton4.place(x=150, y=600, width=50, height=50)

bouton5 = tk.Button(fenetre, text="5", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum("5"))
bouton5.place(x=200, y=600, width=50, height=50)

bouton6 = tk.Button(fenetre, text="6", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum("6"))
bouton6.place(x=250, y=600, width=50, height=50)

bouton7 = tk.Button(fenetre, text="7", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum("7"))
bouton7.place(x=300, y=600, width=50, height=50)

bouton8 = tk.Button(fenetre, text="8", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum("8"))
bouton8.place(x=350, y=600, width=50, height=50)

bouton9 = tk.Button(fenetre, text="9", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum("9"))
bouton9.place(x=400, y=600, width=50, height=50)

bouton0 = tk.Button(fenetre, text="0", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum("0"))
bouton0.place(x=450, y=600, width=50, height=50)

#boutons d'action
btn_annuler = tk.Button(fenetre, text="Annule", bd=0.5, font=("helvetica", 15), fg="red", command=lambda:pressLettre("annuler"))
btn_annuler.place(x=500, y=600, width=80, height=50)

btn_retourner = tk.Button(fenetre, text="Retourne", bd=0.5, font=("helvetica", 15), fg="red", command=lambda:pressLettre("retourner"))
btn_retourner.place(x=580, y=600, width=100, height=50)

#créer des fonctions
lists = []
isPressNum = False

#fonction de chiffres
def pressNum(num):
    global lists
    global isPressNum
    oldnum = result.get()
    if oldnum == "0":
        result.set(num)#si on appuie sur 0, alors il affiche "0"
    else:
        newnum= oldnum + num#si on a pas appuie sur 0, alors il affiche "0" plus le nombre qu'on a appuié
        result.set(newnum)



def pressLettre(lettre):
    if lettre == "annuler":
        lists.clear()
        result.set(" ")
    if lettre == "retourner":
        lists.clear()
        result.set(" ")

fenetre.mainloop()

