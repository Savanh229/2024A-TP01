# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math

speed = float(input("Quelle est la vitesse du projectile en m/s?"))
angle = float(input("Quelle est l'angle du projectile en degrés ?"))
x=speed
y=angle
g=9.8
portee=round((pow(x,2)*math.sin(math.radians(2*y)))/g,2)

print("La distance maximale en x est de ",portee, "m")