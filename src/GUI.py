import tkinter as tk
from tkinter import messagebox

class GUI:
    def __init__(self):
        # Initialisation de la fenêtre
        self.window = tk.Tk()
        self.window.geometry("400x200")
        self.window.title("Programme d'installation")

        # Ajout d'un label pour afficher les messages
        self.label = tk.Label(self.window, text="", font=("Helvetica", 14))
        self.label.pack(pady=20)

    # Fonction pour mettre à jour le label
    def update_label(self, text):
        self.label.configure(text=text)

    # Fonction pour afficher une boîte de dialogue de confirmation
    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    # Fonction pour fermer la fenêtre
    def close(self):
        self.window.destroy()
