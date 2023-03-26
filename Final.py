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



# Cette fonction sert à mélanger les lignes dans une même rangée de 3 

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

# Cette fonction sert à mélanger les colonnes dans une même rangée de 3

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

# Fonctions pour les boutons des chiffres

lists = []

def pressNum(num):
    oldnum = result.get()
    if oldnum == "0":
        result.set(num) #si oldnum = 0, on obtient le nombre qu'on vas appuyer après
    else:
        newnum= oldnum + num #si oldnum != 0, on obtient le nombre qu'on a appuyé plus le nombre qu'on a appuyé la deuxième fois
        result.set(newnum)

def pressLettre(lettre):
    global lists
    if lettre == "annuler":
        lists.clear()
        result.set(" ")
    if lettre == "retourner":
        lists.clear()
        result.set(" ")




# Création de la fenêtre

Taille = 600
Case = 9

fenetre = tk.Tk()
fenetre.title("Sudoku")
fenetre.geometry("700x700")

result = tk.StringVar()

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


#Création des boutons des chiffres

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

#Création des boutons d'action

btn_annuler = tk.Button(fenetre, text="Annule", bd=0.5, font=("helvetica", 15), fg="red", command=lambda:pressLettre("annuler"))
btn_annuler.place(x=450, y=600, width=80, height=50)

btn_retourner = tk.Button(fenetre, text="Retourne", bd=0.5, font=("helvetica", 15), fg="red", command=lambda:pressLettre("retourner"))
btn_retourner.place(x=530, y=600, width=100, height=50)


# Bouton pour commencer la partie

def affichage(Grille):
    a = mélangerlignes(Grille)
    b = mélangercolonnes(a)
    c = cryptage(b)
    hasard = 0

    for n in range(len(c)):
        for t in range(len(c)):
            position = grille.create_text((Taille-565)+(t*(Taille-533)), (Taille-570)+(n*(Taille-533)), text= str(c[n][t]), font="35")
    
    while hasard != 30:
        r = rd.randint(0, 8)
        e = rd.randint(0, 8)
        affichage = tk.Label(grille, bg= "grey79", font= "35", relief="solid", textvariable= result)
        affichage.place(x=(r*Taille)/Case , y= (e*Taille)/Case, width=67, height=67)
        hasard += 1

    


lancement = tk.Button(fenetre, command= lambda : affichage(G1), text= "On commence ?")
lancement.grid(row= 0, column= 1)

fenetre.mainloop()