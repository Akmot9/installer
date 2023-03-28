import psutil                                                                # Importe la bibliothèque psutil qui permet d'accéder aux informations système, notamment les services Windows
class CheckService:                                                          # Définit une classe nommée "CheckService" qui va contenir les méthodes de vérification de service
    def __init__(self):                                                      # Définit la méthode "constructeur" de la classe qui sera appelée à l'instanciation de la classe
        self.services = list(psutil.win_service_iter())                      # Récupère la liste des services Windows en utilisant la méthode "win_service_iter()" de la bibliothèque psutil et la stocke dans la variable "self.services"
    def is_present(self, service_name):                                      # Définit une méthode nommée "is_present" qui prend en paramètre le nom d'un service
        for service in self.services:                                        # Pour chaque service de la liste "self.services"
            if service_name.lower() in service.name().lower():               # Si le nom du service recherché (en minuscules) est contenu dans le nom du service de la liste (en minuscules)
                print(f"Le service {service_name} est présent sur votre PC.")# Affiche un message indiquant que le service recherché est présent
                return True                                                  # Renvoie "True" pour indiquer que le service est présent
        print(f"Le service {service_name} n'est pas présent sur votre PC.")  # Si le service n'a pas été trouvé, affiche un message indiquant qu'il n'est pas présent
        return False                                                         # Renvoie "False" pour indiquer que le service n'est pas présent

