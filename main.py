"""def demander_information(nom, age):
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


#nom1 = demander_nom()
#nom2 = demander_nom()
#age1 = demander_age(nom1)
#age2 = demander_age(nom2)

#demander_information(nom1, age1)
#demander_information(nom2, age2)

NOMBRE_PERSONNES = 5

for i in range(0, NOMBRE_PERSONNES):
    nom = input("Entrer votre nom: ")
    age = demander_age(nom)
    demander_information(nom, age)


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")

    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre age ? ")

        try:
            age_int = int(age_str)
        except ValueError:
            print("Erreur: Vous devez entrer un nombre pour l'age")
    return age_int


def afficher_information(nom, age):
    print()
    print("Vous vous appelez " + nom + " vous avez " + str(age) + "ans")

    if 1 <= age < 3:
        print("Vous etes bébé!")
    elif age < 10:
        print("Vous etes mineur!")
    elif age == 17:
        print("Vous etes presque majeur!")
    elif 10 <= age < 18:
        print("vous etes adolescent!")
    elif age == 18:
        print("Tout juste majeur: felicitations!")
    elif age > 60:
        print("Vous etes senior!")
    elif age >= 18:
        print("Vous etes majeur!")
    else:
        print("Information no valide!")
    print("L'an prochain vous aurez " + str(age + 1) + "ans")


NOMBRE_PERSONNE = int(input("Entrer le nombre de personne: "))
for i in range(0, NOMBRE_PERSONNE):
    nom = demander_nom()
    age = demander_age(nom)
    afficher_information(nom, age)"""

import turtle

t = turtle.Turtle()


def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)


carre(25)
carre(50)
carre(75)
carre(100)
carre(125)
carre(150)
carre(175)
carre(200)



turtle.done()















