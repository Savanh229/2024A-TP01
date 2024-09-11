# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
10
water_quantity = int(input("Quelle est la quantité d'eau en litres ?"))
x= water_quantity
filtre= x/5
lampe= 3*x/5
chlore= x/10
print("Voici les quantités nécessaires pour",x, "L d'eau:")
print(int(filtre), "filtres", int(lampe), "lampes UV", chlore, "kg de chlore")
