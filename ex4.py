# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Pourcentage de batterie ? "))
x=battery_level
if battery_level >= 50:
    distance= 2*(battery_level-50)+25*0.5+15*1+5*2.5+5*6
elif 25< battery_level <= 50:
    distance= 0.5*(battery_level-25)+15*1+5*2.5+5*6
elif 10< battery_level<=25:
    distance=(battery_level-10)+5*2.5+5*6
elif 5< battery_level <=10:
    distance=2.5*(battery_level-5)+5*6
elif battery_level<= 5:
    distance= 6*battery_level

if battery_level==0:
    print("La batterie est vide")
else:
    (print(f"{distance} km"))




