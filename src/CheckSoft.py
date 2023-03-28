import subprocess
import winreg

class CheckInstalledPrograms:
    def __init__(self):
        self.installed_programs = self.get_installed_programs()

    def get_installed_programs(self):
        # Méthode 1 : Utilisation de subprocess
        installed_programs = subprocess.check_output(['wmic', 'product', 'get', 'name'])
        installed_programs = installed_programs.decode('cp1252', 'ignore')
        installed_programs = installed_programs.split('\n')
        installed_programs = [x.strip() for x in installed_programs if x.strip()]

        # Méthode 2 : Utilisation de winreg
        uninstall_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
            0,
            winreg.KEY_READ | winreg.KEY_WOW64_32KEY)

        count_subkey = winreg.QueryInfoKey(uninstall_key)[0]

        for i in range(count_subkey):
            subkey_name = winreg.EnumKey(uninstall_key, i)
            subkey = winreg.OpenKey(uninstall_key, subkey_name)
            try:
                display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                installed_programs.append(display_name)
            except OSError:
                pass

        return installed_programs

    def is_installed(self, software_name):
        for program in self.installed_programs:
            if software_name.lower() in program.lower():
                print(f"{software_name} est installé sur cet ordinateur.")
                return True
        print(f"{software_name} n'est pas installé sur cet ordinateur.")
        return False
