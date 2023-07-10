def demander_information(nom, age):
    print()
    print("\nvous vous appelez " + nom + " vous avez " + str(age) + "ans")
    print("L'an prochaine vous aurez " + str(age + 1) + "ans\n")

    if age < 10:
        print("vous etes enfant!")
    elif age == 17:
        print("vous etes presque majeur!")
    elif age == 18:
        print("tout juste majeur: felicitations!")
    elif age > 60:
        print("vous etes senior!")
    elif age >= 18:
        print("vous etes majeur!")
    else:
        print("vous etes mineur!")



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
age1 = demander_age(nom1)
age2 = demander_age(nom2)

demander_information(nom1, age1)
demander_information(nom2, age2)
















