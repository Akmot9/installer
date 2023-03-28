import tkinter as tk
from src.CheckSoft import CheckInstalledPrograms
from src.CheckService import CheckService


class GUI:
    def __init__(self):
        self.installed_programs = CheckInstalledPrograms()
        self.services = CheckService()

        # Créer la fenêtre principale
        self.root = tk.Tk()
        self.root.title("Déploiment Logiciel")
        self.root.geometry("400x400")

        # Afficher la fenêtre
        self.root.mainloop()