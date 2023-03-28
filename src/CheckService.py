import psutil

class CheckService:
    def __init__(self):
        self.services = list(psutil.win_service_iter())

    def is_present(self, service_name):
        for service in self.services:
            if service_name.lower() in service.name().lower():
                print(f"Le service {service_name} est présent sur votre PC.")
                return True
        print(f"Le service {service_name} n'est pas présent sur votre PC.")
        return False
