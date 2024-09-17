# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math

speed = float(input("Vitesse initiale (m/s): "))
angle = float(input("Angle de lancer (en degrés): "))
x=speed
y=angle
g=9.8
portee=round((pow(x,2)*math.sin(math.radians(2*y)))/g,2)

print(f"Distance parcourue: {portee}m")