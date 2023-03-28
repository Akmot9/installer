from CheckSoft import CheckInstalledPrograms
from CheckService import CheckService
from GUI import GUI

window = GUI()

# Instancier un objet CheckInstalledPrograms
program_checker = CheckInstalledPrograms()
# Liste des programmes à vérifier
programs_to_check = [
    "PDF Creator",
    "Mozilla Firefox",
    "7-Zip"
]
# Vérifier chaque programme dans la liste
for program in programs_to_check:
    program_checker.is_installed(program)

# Instancier un objet CheckService
service_checker = CheckService()
# Liste des services à vérifier
services_to_check = [
    "ELK",
    "KIBANA"
]
# Vérifier chaque service dans la liste
for service in services_to_check:
    service_checker.is_present(service)



