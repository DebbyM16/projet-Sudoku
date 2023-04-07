import tkinter as tk
import time
import winsound
import tkinter.messagebox

#PARAMETRES:
#heure début
time_start=[0,1,5]
text_font = ("helvetica", 150)
text_color = "black"
color_bg = "white"

#clavier
def event_key(event):
    global count_state,win_main
    #print('key: ' + event.keysym+" event:"+str(event) )
    if event.keysym=='Escape':
       win_main.attributes("-fullscreen", False)
    elif event.keysym=='F11':
       win_main.attributes("-fullscreen", True)
    elif event.keysym=='Left':
        if count_state == 2:
            count_state = 3
    elif event.keysym=='Right':
        if count_state != 2:
            count_state = 1
    elif event.keysym=='Up':
        count_state = 0
    fenetre.mainloop()
#mise à jours l'heure
def time_update():
    global time_start,count_state,count_length,count_gap,count_start,text_time,win_main
    if count_state == 0:
        count_length = int(time_start[0])*3600+int(time_start[1])*60+int(time_start[2])
        count_gap = count_length
    elif count_state == 1:
        count_start = time.time()
        count_state = 2
    elif count_state == 2:
        count_gap = max( 0, count_length-int(time.time()-count_start) )
        if count_gap <= 0:
            winsound.Beep( 2000, 1000 )
            count_state = 4
    elif count_state == 3:
        count_length = count_gap
        count_state = 4
    count_now = str(int(((count_gap)%86400)/3600))+":"
    count_now = count_now + str(int(((count_gap)%3600)/60))+":"
    count_now = count_now + str(int((count_gap)%60))
    text_time["text"] = count_now
    fenetre.after(100, time_update)
#heure de départ
count_state = 0

Taille = 600
Case = 9
fenetre = tk.Tk()
fenetre.title("Sudoku")
fenetre.configure(bg=color_bg)
fenetre.geometry("1000x700")
fenetre.bind('<Key>', event_key)
text_time = tk.Label(fenetre, text="TIME SHOW", font=("helvetica", 30), fg=text_color, bg="grey" )
text_time.place(x=800, y=0, width=150, height=67)
fenetre.after(100, time_update)

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
affichage = tk.Label(grille, font=("helvetica", 30), bg="grey", bd="9", fg="black", textvariable=result) #lorsqu'on a changé les chiffres de l'écran, "result" vas prendre valeurs qu'on a changé
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
#fonction de chiffres
def pressNum(num):
    oldnum = result.get()
    if oldnum == "0":
        result.set(num)#si oldnum = 0, on obtient le nombre qu'on vas appuyer après
    else:
        newnum= oldnum + num#si oldnum égale pas à 0, on obtient le nombre qu'on a appuyé plus le nombre qu'on a appuyé la deuxième fois
        result.set(newnum)




def pressLettre(lettre):
    global lists
    if lettre == "annuler":
        lists.clear()
        result.set(" ")
    if lettre == "retourner":
        lists.clear()
        result.set(" ")

# définir une bouton d'alerte
def alerte():
    tkinter.messagebox.showerror(title="Alerte aux erreurs", message="Désolé, vous avez fait une erreur!")
    return "True", "False"

alerte=tk.Button(fenetre, text="Cliquer", bg="grey", font=("helvetica", 15), command=alerte)
alerte.place(x=610, y=200, width=80, height=50)


fenetre.mainloop()
