import tkinter as tk
from tkinter.colorchooser import askcolor
import json

def changer_couleur(event):
    couleur = askcolor()[1]
    if couleur:
        event.widget.config(bg=couleur)
        sauvegarder_etat()

def sauvegarder_etat():
    etat = [[p.cget('bg') for p in ligne] for ligne in pixels]
    with open('etat_pixels.json', 'w') as f:
        json.dump(etat, f)

def charger_etat():
    try:
        with open('etat_pixels.json', 'r') as f:
            etat = json.load(f)
            for i in range(nb_pixels):
                for j in range(nb_pixels):
                    pixels[i][j].config(bg=etat[i][j])
    except FileNotFoundError:
        print("Aucun fichier d'état trouvé.")

root = tk.Tk()
root.title("Coloriage de Pixels")

# Définir la taille du rectangle et le nombre de pixels
largeur, hauteur = 400, 400
nb_pixels = 10

# Créer une grille de pixels
taille_pixel = largeur // nb_pixels
pixels = [[tk.Frame(root, width=taille_pixel, height=taille_pixel, bd=1, relief='solid') for _ in range(nb_pixels)] for _ in range(nb_pixels)]

# Placer les pixels dans la fenêtre
for i in range(nb_pixels):
    for j in range(nb_pixels):
        pixels[i][j].grid(row=i, column=j)

# Charger l'état s'il existe
charger_etat()

# Associer la fonction changer_couleur à chaque pixel
for i in range(nb_pixels):
    for j in range(nb_pixels):
        pixels[i][j].bind("<Button-1>", changer_couleur)

while True:
    root.update()
