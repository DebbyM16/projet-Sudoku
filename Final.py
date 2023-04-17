import tkinter as tk
import random as rd
from tkinter import ttk



""" Variables pour les fonctions et l'interface graphique """ 


# Grille de base 

G1 = [[9, 1, 4, 5, 2, 3, 8, 7, 6],  
      [3, 7, 5, 9, 6, 8, 4, 2, 1], 
      [6, 2, 8, 7, 1, 4, 3, 5, 9], 
      [2, 9, 6, 4, 5, 1, 7, 8, 3], 
      [5, 8, 3, 6, 7, 2, 9, 1, 4], 
      [1, 4, 7, 8, 3, 9, 5, 6, 2], 
      [4, 6, 9, 1, 8, 7, 2, 3, 5], 
      [7, 3, 1, 2, 4, 5, 6, 9, 8], 
      [8, 5, 2, 3, 9, 6, 1, 4, 7]]

# Listes vides

nouvelle_grille = []
hasard = []

# Variables pour l'interface

Taille = 600
Case = 9

# Variables diverses

end = True
boucle = 0
value = None
X,Y = None, None



""" Fonctions """


# Cette fonction sert à mélanger les lignes de la grille dans une même rangée de 3 

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

# Cette fonction sert à mélanger les colonnes de la grille dans une même rangée de 3

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

# Cette fonction sert à crypter la grille grâce à une clé de cryptage prise au hasard 

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

# Cette fonction crée les cases à remplir

def create_entry(canvas, i, j):
    global Taille, Case
    
    a_remplir = tk.IntVar(canvas, " ")
    a_remplir.trace("w", test_erreur)
    
    def focus(*args, v= a_remplir, x= j, y= i):
        global value, X, Y
        
        value = v
        X,Y = x,y

    affichage = tk.Entry(canvas, bg= "grey79", fg= "violet red" , font= "35", relief= "solid", justify= "center", textvariable= a_remplir)
    affichage.bind('<FocusIn>', focus)
    affichage.place(x= (i*Taille)/Case , y= (j*Taille)/Case, width= 67, height= 67)

# Cette fonction rempli une case quand on appuye sur un bouton "chiffre"

def pressNum(num):
    global value
    
    value.set(num)

# Cette fonction efface un chiffre rentré dans une case

def pressLettre():
    global value
    
    value.set(" ")

# Cette fonction vérifie que les chiffres sont les bons et informe quand la partie est terminée

def test_erreur(*args):
    global value, nouvelle_grille, X, Y, message_erreur, hasard, end

    if value.get() != nouvelle_grille[X][Y]:
        message_erreur.set("ERREUR")
    else:
        message_erreur.set('')
        hasard.remove((X,Y))
        if hasard == []:
            end = False
            finish = tk.Label(fenetre, relief= "groove", fg = 'red', text= "BRAVO ! Vous avez gagné !")
            finish.grid(row= 0, column= 0, columnspan= 10)

# Cette fonction remplie une case à la demande du joueur

def aide():
    global nouvelle_grille, X, Y, message_erreur
    
    pressNum(nouvelle_grille[X][Y])
    message_erreur.set('')

# Cette fonction arrête le chrononomètre pour mettre le jeu en pause

def pause():
    global end
    
    end = False

# Cette fonction relance le chronomètre quand le jeu est en pause

def reparti():
    global end
    
    end = True
    loop()

# Cette fonction affiche les chiffres et les cases à remplir dans l'interface

def affichage(Grille):
    global nouvelle_grille, hasard

    nouvelle_grille = cryptage(melangercolonnes(melangerlignes(Grille)))

    for i in range(30):
        generate_case(hasard)
    
    for n in range(len(nouvelle_grille)):
        for t in range(len(nouvelle_grille)):
            if (n, t) in hasard:
                create_entry(grille, t, n)
            else:
                x = (Taille-565)+(t*(Taille-533))
                y = (Taille-570)+(n*(Taille-533))
                position = grille.create_text(x, y, text= str(nouvelle_grille[n][t]), font= "35")

# Cette fonction fait tourner le chronomètre

def loop():
    global fenetre, compteur, boucle, end

    boucle += 1
    minutes = boucle // 60
    secondes = boucle % 60
    compteur.set(str(minutes) + " : " + str(secondes))
    if end == True:
        fenetre.after(1000, loop)

# Cette fonction lance la partie et rend les boutons cliquables

def start():
    affichage(G1)
    loop()

    bouton1["state"] = "normal"
    bouton2["state"] = "normal"
    bouton3["state"] = "normal"
    bouton4["state"] = "normal"
    bouton5["state"] = "normal"
    bouton6["state"] = "normal"
    bouton7["state"] = "normal"
    bouton8["state"] = "normal"
    bouton9["state"] = "normal"
    btn_annuler["state"] = "normal"
    btn_aide["state"] = "normal"
    btn_pause["state"] = "normal"
    btn_reparti["state"] = "normal"



""" Interface graphique """


# Mise en forme de la fenêtre

fenetre = tk.Tk()
fenetre.title("Sudoku")
fenetre.geometry("700x700")

bis = ttk.Frame(fenetre)
bis.rowconfigure(0, weight= 1)
bis.rowconfigure(5, weight= 1)
bis.grid(row= 0, column= 10, sticky= 'ns')

grille = tk.Canvas(fenetre, height= Taille, width= Taille)
grille.grid(row= 0, column= 0, columnspan= 10)

# Message d'erreur

message_erreur = tk.StringVar(fenetre)
erreur = tk.Label(bis, textvariable= message_erreur, fg= 'red', relief= "sunken")
erreur.grid(row= 1, column= 0)

# Chronomètre

compteur = tk.StringVar(fenetre, "0 : 0")
chrono = tk.Label(bis, relief= "sunken", font= "35", textvariable= compteur)
chrono.grid(row= 0, column= 0)

# Création de la grille

for i in range(Case+1):
    if i % 3 == 0:
        verticale = grille.create_line((i*Taille)/Case, 0, (i*Taille)/Case, Taille, width= 3)
        horizontale = grille.create_line(0,(i*Taille)/Case, Taille, (i*Taille)/Case, width= 3)
    else:
        verticale = grille.create_line((i*Taille)/Case, 0, (i*Taille)/Case, Taille)
        horizontale = grille.create_line(0,(i*Taille)/Case, Taille, (i*Taille)/Case)

# Boutons "chiffres"

bouton1 = tk.Button(fenetre, text= "1", font= ("helvetica", "20"), fg= "black", bd= 0.5, command= lambda : pressNum(1), state= "disable")
bouton1.grid(row= 1, column= 0)

bouton2 = tk.Button(fenetre, text= "2", font= ("helvetica", "20"), fg= "black", bd= 0.5, command= lambda : pressNum(2), state= "disable" )
bouton2.grid(row= 1, column= 1)

bouton3 = tk.Button(fenetre, text= "3", font= ("helvetica", "20"), fg= "black", bd= 0.5, command= lambda : pressNum(3), state= "disable" )
bouton3.grid(row= 1, column= 2)

bouton4 = tk.Button(fenetre, text= "4", font= ("helvetica", "20"), fg= "black", bd= 0.5, command= lambda : pressNum(4), state= "disable")
bouton4.grid(row= 1, column= 3)

bouton5 = tk.Button(fenetre, text= "5", font= ("helvetica", "20"), fg= "black", bd= 0.5, command= lambda : pressNum(5), state= "disable")
bouton5.grid(row= 1, column= 4)

bouton6 = tk.Button(fenetre, text= "6", font= ("helvetica", "20"), fg= "black", bd= 0.5, command= lambda : pressNum(6), state= "disable")
bouton6.grid(row= 1, column= 5)

bouton7 = tk.Button(fenetre, text= "7", font= ("helvetica", "20"), fg= "black", bd= 0.5, command= lambda : pressNum(7), state= "disable")
bouton7.grid(row= 1, column= 6)

bouton8 = tk.Button(fenetre, text= "8", font= ("helvetica", "20"), fg= "black", bd= 0.5, command= lambda : pressNum(8), state= "disable")
bouton8.grid(row= 1, column= 7)

bouton9 = tk.Button(fenetre, text= "9", font= ("helvetica", "20"), fg= "black", bd= 0.5, command= lambda : pressNum(9), state= "disable")
bouton9.grid(row= 1, column= 8)

# Bouton d'annulation

btn_annuler = tk.Button(fenetre, text= "Annuler", font= ("helvetica", "15"), fg= "red", bd= 0.5, command= lambda : pressLettre(), state= "disable")
btn_annuler.grid(row= 1, column= 9)

# Bouton d'aide 

btn_aide = tk.Button(fenetre, text= "Aide", font= ("helvetica", "15"), fg= "red", bd= 0.5, command= lambda : aide(), state= "disable")
btn_aide.grid(row= 1, column= 10)

# Boutons de pause et de reprise du jeu

btn_pause = tk.Button(bis, text= "Pause", command= lambda : pause(), state= "disable")
btn_pause.grid(row= 3, column= 0)

btn_reparti = tk.Button(bis, text= "Relancer la partie", command= lambda : reparti(), state= "disable")
btn_reparti.grid(row= 4, column= 0)

# Bouton pour commencer la partie

lancement = tk.Button(bis, text= "Jouer", command= lambda : start())
lancement.grid(row= 2, column= 0)

fenetre.mainloop()