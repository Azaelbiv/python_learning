
def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("Erreur: vous devez rentrer un nombre pour l'age.")
    return age_int


nom1 = demander_nom()
nom2 = demander_nom()
nom3 = demander_nom()
age1 = demander_age(nom1)
age2 = demander_age(nom2)
age3 = demander_age(nom3)
print("\nvous vous appelez " + nom1 + " vous avez " + str(age1) + "ans")
print("L'an prochaine vous aurez " + str(age1+1) + "ans\n")

print("\nvous vous appelez " + nom2 + " vous avez " + str(age2) + "ans")
print("L'an prochaine vous aurez " + str(age2+1) + "ans\n")

print("\nvous vous appelez " + nom3 + " vous avez " + str(age3) + "ans")
print("L'an prochaine vous aurez " + str(age3+1) + "ans\n")












