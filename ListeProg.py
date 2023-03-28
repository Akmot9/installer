import winreg


class CheckSoft:
    def __init__(self):
        # Ouvrir la clé de désinstallation
        self.uninstall_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
            0,
            winreg.KEY_READ | winreg.KEY_WOW64_32KEY)

    def is_installed(self, software_name):
        # Compter le nombre de sous-clés dans la clé de désinstallation
        count_subkey = winreg.QueryInfoKey(self.uninstall_key)[0]

        # Chercher le logiciel dans les sous-clés
        software_present = False

        for i in range(count_subkey):
            subkey_name = winreg.EnumKey(self.uninstall_key, i)
            subkey = winreg.OpenKey(self.uninstall_key, subkey_name)
            try:
                display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                if software_name in display_name:
                    software_present = True
            except OSError:
                pass

        # Afficher le résultat de la détection
        if software_present:
            print(f"{software_name} est installé sur cet ordinateur.")
            return True
        else:
            print(f"{software_name} n'est pas installé sur cet ordinateur.")
            return False


# Instancier un objet CheckSoft
checker = CheckSoft()

# Détecter PERISCOP
checker.is_installed("PERISCOP")

# Détecter PDF Creator
checker.is_installed("PDF Creator")
