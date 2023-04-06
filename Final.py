import tkinter as tk
import random as rd
from tkinter import ttk



G1 = [[9, 1, 4, 5, 2, 3, 8, 7, 6] ,  
      [3, 7, 5, 9, 6, 8, 4, 2, 1] , 
      [6, 2, 8, 7, 1, 4, 3, 5, 9] , 
      [2, 9, 6, 4, 5, 1, 7, 8, 3] , 
      [5, 8, 3, 6, 7, 2, 9, 1, 4] , 
      [1, 4, 7, 8, 3, 9, 5, 6, 2] , 
      [4, 6, 9, 1, 8, 7, 2, 3, 5] , 
      [7, 3, 1, 2, 4, 5, 6, 9, 8] , 
      [8, 5, 2, 3, 9, 6, 1, 4, 7]]



# Cette fonction sert à mélanger les lignes dans une même rangée de 3 

def melangerlignes(G):
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

# Cette fonction sert à mélanger les colonnes dans une même rangée de 3

def melangercolonnes(G):
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

# Cette fonction sert à crypter une grille grâce à une clé de cryptage prise au hasard 

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

#  Cette fonction génère les coordonnées des cases à remplir sans doublons

def generate_case(liste):
    x = rd.randint(0, 8)
    y = rd.randint(0, 8)

    while (x,y) in liste:
        x,y = rd.randint(0, 8), rd.randint(0, 8)
    
    liste.append((x,y))

# Cette fonction créée les cases à remplir 

value = None
X,Y = None, None

def create_entry(canvas, i, j):
    global Taille, Case
    a_remplir = tk.IntVar(canvas)
    a_remplir.trace("w", test_erreur)
    
    def focus(*args, v=a_remplir, x=j, y=i):
        global value, X, Y
        value = v
        X,Y = x,y

    affichage = tk.Entry(canvas, bg= "grey79", fg= "violet red" , font= "35", relief="solid", justify= "center", textvariable= a_remplir)
    affichage.bind('<FocusIn>', focus)
    affichage.place(x=(i*Taille)/Case , y= (j*Taille)/Case, width=67, height=67)


# Fonctions pour les boutons des chiffres

lists = []

def pressNum(num):
    global value
    value.set(num)

def test_erreur(*args):
    global value, c, X, Y, message_erreur

    if value.get() != c[X][Y]:
        message_erreur.set("ERREUR")
    else:
        message_erreur.set('')


def pressLettre(lettre):
    global lists, value
    if lettre == "annuler":
        lists.clear()
        value.set(" ")
    if lettre == "retourner":
        lists.clear()
        value.set(" ")




# Création de la fenêtre

Taille = 600
Case = 9

fenetre = tk.Tk()
fenetre.title("Sudoku")
fenetre.geometry("700x700")

bis = ttk.Frame(fenetre)
bis.rowconfigure(0, weight= 1)
bis.rowconfigure(3, weight= 1)
bis.grid(row=0, column=11, sticky= 'ns')

message_erreur = tk.StringVar(fenetre)
erreur = tk.Label(bis, textvariable= message_erreur, fg= 'red')
erreur.grid(row=1, column=0)

grille = tk.Canvas(fenetre, height= Taille, width= Taille)
grille.grid(row= 0, column= 0, columnspan= 11)

# Création de la grille

for i in range(Case+1):
    if i % 3 == 0:
        verticale = grille.create_line((i*Taille)/Case, 0, (i*Taille)/Case, Taille, width= 3)
        horizontale = grille.create_line(0,(i*Taille)/Case, Taille, (i*Taille)/Case, width= 3)
    else:
        verticale = grille.create_line((i*Taille)/Case, 0, (i*Taille)/Case, Taille)
        horizontale = grille.create_line(0,(i*Taille)/Case, Taille, (i*Taille)/Case)


#Création des boutons des chiffres

bouton1 = tk.Button(fenetre, text="1", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum(1))
bouton1.grid(row=1, column=0)

bouton2 = tk.Button(fenetre, text="2", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum(2))
bouton2.grid(row=1, column=1)

bouton3 = tk.Button(fenetre, text="3", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum(3))
bouton3.grid(row=1, column=2)

bouton4 = tk.Button(fenetre, text="4", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum(4))
bouton4.grid(row=1, column=3)

bouton5 = tk.Button(fenetre, text="5", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum(5))
bouton5.grid(row=1, column=4)

bouton6 = tk.Button(fenetre, text="6", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum(6))
bouton6.grid(row=1, column=5)

bouton7 = tk.Button(fenetre, text="7", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum(7))
bouton7.grid(row=1, column=6)

bouton8 = tk.Button(fenetre, text="8", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum(8))
bouton8.grid(row=1, column=7)

bouton9 = tk.Button(fenetre, text="9", font=("helvetica", 20), fg=("black"), bd=0.5, command=lambda:pressNum(9))
bouton9.grid(row=1, column=8)

#Création des boutons d'action

btn_annuler = tk.Button(fenetre, text="Annule", bd=0.5, font=("helvetica", 15), fg="red", command=lambda:pressLettre("annuler"))
btn_annuler.grid(row=1, column=9)

btn_retourner = tk.Button(fenetre, text="Retourne", bd=0.5, font=("helvetica", 15), fg="red", command=lambda:pressLettre("retourner"))
btn_retourner.grid(row=1, column=10)


# Bouton pour commencer la partie
c = []
def affichage(Grille):
    global c
    
    a = melangerlignes(Grille)
    b = melangercolonnes(a)
    c = cryptage(b)
    hasard = []

    for i in range(30):
        generate_case(hasard)
    
    for n in range(len(c)):
        for t in range(len(c)):
            if (n, t) in hasard:
                create_entry(grille, t, n)
            else:
                x = (Taille-565)+(t*(Taille-533))
                y = (Taille-570)+(n*(Taille-533))
                position = grille.create_text(x, y, text= str(c[n][t]), font="35")
    

   
            
    
lancement = tk.Button(bis, command= lambda : affichage(G1), text= "On commence ?")
lancement.grid(row= 2, column= 0)

fenetre.mainloop()