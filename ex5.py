#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")
if not all(character in ["G", "S", "B"] for character in code_medals):
    print("Un caractère est invalide")
else:
    a=(code_medals.count("G"))
    b= (code_medals.count("S"))
    c= (code_medals.count("B"))

print(f"{country}:\n- {a} OR\n- {b} Argent\n- {c} Bronze")
