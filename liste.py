import winreg

def get_installed_programs():
    installed_programs = []
    uninstall_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall")
    num_subkeys = winreg.QueryInfoKey(uninstall_key)[0]
    for i in range(num_subkeys):
        subkey_name = winreg.EnumKey(uninstall_key, i)
        subkey = winreg.OpenKey(uninstall_key, subkey_name)
        try:
            display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
            installed_programs.append(display_name)
        except OSError:
            pass
        subkey.Close()
    return installed_programs

if __name__ == "__main__":
    programs = get_installed_programs()
    for program in programs:
        print(program)

# Liste des programmes à vérifier
    programs_to_check = [
        "PDF Creator",
        "Mozilla Firefox",
        "7-Zip"
    ]
    # Liste des services à vérifier
    services_to_check = [
        "ELK",
        "KIBANA"
    ]

    program_checker = CheckInstalledPrograms()
    # Vérifier chaque programme dans la liste
    for program in programs_to_check:
        program_checker.is_installed(program)

    service_checker = CheckService()
    # Vérifier chaque service dans la liste
    for service in services_to_check:
        service_checker.is_present(service)