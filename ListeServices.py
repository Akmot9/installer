import psutil
import re

# Liste de tous les services sur l'ordinateur
services = list(psutil.win_service_iter())

# Vérification de la présence des services ELK et Kibana
elk_present = False
kibana_present = False
for service in services:
    if re.search(r"ELK", service.name(), re.IGNORECASE):
        elk_present = True
    elif re.search(r"KIBANA", service.name(), re.IGNORECASE):
        kibana_present = True

if elk_present:
    print("Le service Elasticsearch est présent sur votre PC.")
else:
    print("Le service Elasticsearch n'est pas présent sur votre PC.")

if kibana_present:
    print("Le service Kibana est présent sur votre PC.")
else:
    print("Le service Kibana n'est pas présent sur votre PC.")
