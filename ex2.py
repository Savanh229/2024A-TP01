# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = input("Quelle quantité d'eau faut-il assainir ? ")

import math
filtre= math.ceil((float(water_quantity)/5))
lampe= math.ceil((float(water_quantity)*(3/5)))
chlore= ((float(water_quantity)/10))
print(f"""Voici les éléments requis pour assainir {water_quantity}L d'eau:\n
        \t- Filtre(s) : {filtre}\n
        \t- Lampe(s) UV : {lampe}\n
        \t- Chlore : {chlore}kg""")