# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quel est le nom de l'athlète?")
date = input("Quel est la date du record?")
discipline= input("Quel est la discipline?")
category= input("Quelle est la catégorie?")
record= input("Quel est le nouveau record?")

print("Nouveau Record:")
print("----------------")
print(date)
print(discipline,"-",category)
print(athlete, country,"-",record)