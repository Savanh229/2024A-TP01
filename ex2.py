# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
10
water_quantity = float(input("Quelle est la quantité d'eau en litres ?"))
x= water_quantity
import math
filtre= math.ceil(x/5)
lampe= math.ceil(3*x/5)
chlore= (x/10)
print("Voici les quantités nécessaires pour",x, "L d'eau:")
print("-",filtre,"filtres")
print("-", lampe,"lampes")
print("-",chlore,"Kg de chlore")