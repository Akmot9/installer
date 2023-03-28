import tkinter as tk
import time


class InstallationStateMachine:
    def __init__(self):
        self.current_state = "welcome"

    def handle_key_event(self, event):
        if event.keysym == "Return":
            self.next_state()

    def next_state(self):
        if self.current_state == "welcome":
            print("Bienvenue !")
            self.current_state = "choose_programs"
        elif self.current_state == "choose_programs":
            print("Sélectionnez les logiciels à installer.")
            self.current_state = "install"
        elif self.current_state == "install":
            print("Installation en cours...")
            self.current_state = "complete"
        elif self.current_state == "complete":
            print("L'installation est terminée !")
        else:
            print("Erreur: état inconnu.")

# Création de la fenêtre principale de l'interface graphique
root = tk.Tk()
root.geometry("300x200")

# Création de la machine à états et ajout d'un label pour afficher l'état actuel
machine = InstallationStateMachine()
state_label = tk.Label(root, text=machine.current_state)
state_label.pack()

# Ajout d'un événement clavier pour passer à l'état suivant
root.bind("<Key>", machine.handle_key_event)

# Boucle principale de l'interface graphique
while True:
    # Mettre à jour l'état actuel affiché dans le label
    state_label.configure(text=machine.current_state)
    # Mettre à jour l'interface graphique
    root.update_idletasks()
    # Pause de 50 millisecondes pour éviter d'utiliser trop de ressources
    time.sleep(0.05)
