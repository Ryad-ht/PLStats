from stats.math import *
import random
import csv
import random

data2 = 'data_2 - data_2.csv'

donnees_liste = []

with open(data2, mode='r', encoding='utf-8') as fichier:
    lecteur_data2 = csv.reader(fichier)
    for ligne in lecteur_data2:
        donnees_liste.append(ligne)

donnees_colonnes = list(zip(*donnees_liste))

# Créer un dictionnaire pour stocker les listes avec des noms
donnees_dict = {}

# Parcourir chaque colonne et l'ajouter au dictionnaire avec le premier élément comme clé
for colonne in donnees_colonnes:  # Exclure la dernière colonne
    nom_colonne = colonne[0]
    donnees_dict[nom_colonne] = list(colonne[1:])

# Afficher les listes nommées
for nom, valeurs in donnees_dict.items():
    print(f"{nom}: {valeurs}")


#maintenant a partir d'ici je veut q'un choix aleatoire s fasse entre des choix de statistique
# Liste des métriques

# Dictionnaire des tests et leurs descriptions
tests = {
    "one-sample t-test": {
        "description": "Teste si la moyenne d'un échantillon unique diffère d'une valeur de population connue.",
        "parametrique": True,
        "variables_categorielles": 0,
        "nombre_modalites": 1,
        "variables_a_tester": 1
    },
    "independent t-test": {
        "description": "Compare les moyennes de deux groupes indépendants.",
        "parametrique": True,
        "variables_categorielles": 1,
        "nombre_modalites": 2,
        "variables_a_tester": 1
    },
    "sign test": {
        "description": "Test non paramétrique pour comparer les médianes de deux échantillons appariés.",
        "parametrique": False,
        "variables_categorielles": 1,
        "nombre_modalites": 2,
        "variables_a_tester": 1
    },
    "Wilcoxon signed-rank test": {
        "description": "Test non paramétrique pour comparer deux échantillons appariés.",
        "parametrique": False,
        "variables_categorielles": 1,
        "nombre_modalites": 2,
        "variables_a_tester": 1
    },
    "Wilcoxon rank-sum test": {
        "description": "Test non paramétrique pour comparer les médianes de deux groupes indépendants.",
        "parametrique": False,
        "variables_categorielles": 1,
        "nombre_modalites": 2,
        "variables_a_tester": 1
    },
    "paired t-test": {
        "description": "Compare les moyennes de deux échantillons appariés.",
        "parametrique": True,
        "variables_categorielles": 1,
        "nombre_modalites": 2,
        "variables_a_tester": 1
    },
    "Kruskal-Wallis": {
        "description": "Version non paramétrique de l'ANOVA pour trois groupes ou plus.",
        "parametrique": False,
        "variables_categorielles": 1,
        "nombre_modalites": 3, # ou plus
        "variables_a_tester": 1
    },
    "ANOVA": {
        "description": "Analyse de variance pour comparer les moyennes de trois groupes ou plus.",
        "parametrique": True,
        "variables_categorielles": 1,
        "nombre_modalites": 3, # ou plus
        "variables_a_tester": 1
    },
    "MANOVA": {
        "description": "Version multivariée de l'ANOVA, teste plusieurs variables de réponse.",
        "parametrique": True,
        "variables_categorielles": 1,
        "nombre_modalites": 3, # ou plus
        "variables_a_tester": 2 # ou plus
    },
    "ANOSIM": {
        "description": "Test non paramétrique pour l'analyse de similarité entre groupes.",
        "parametrique": False,
        "variables_categorielles": 1,
        "nombre_modalites": 2, # ou plus
        "variables_a_tester": 1
    }
}

# Sélection aléatoire d'un test
choix_test = random.choice(list(tests.keys()))

# Affichage des détails du test choisi
details_test = tests[choix_test]
print(f"Test sélectionné : {choix_test}")
print(f"Description : {details_test['description']}")
print(f"Paramétrique : {'Oui' if details_test['parametrique'] else 'Non'}")
print(f"Nombre de variables catégorielles : {details_test['variables_categorielles']}")
print(f"Nombre de modalités : {details_test['nombre_modalites']}")
print(f"Nombre de variables à tester : {details_test['variables_a_tester']}")






# #V2
# # Demander à l'utilisateur de saisir la taille de la liste
# taille_liste = input("Veuillez entrer la taille de la liste que vous souhaitez : ")
# # S'assurer que la saisie est un nombre entier valide
# try:
#     taille_liste = int(taille_liste)
#     if taille_liste < 0:
#         print("Veuillez entrer un nombre entier positif.")
#     else:
#         # Créer et remplir la liste avec des nombres aléatoires
#         liste_utilisateur = [random.randint(0, 100) for _ in range(taille_liste)]
#         print(f"Voici votre liste de nombres aléatoires : {liste_utilisateur}")
#
#         while True:
#             choix = input("Entrez le nom de la fonction (median, mean, min, max, range, std, variance, quartiles, eqr) ou 'quit' pour quitter : ").lower()
#
#             if choix == 'median':
#                 print("La médiane est " + str(median(liste_utilisateur)))
#             elif choix == 'mean':
#                 print("La moyenne est " + str(calculate_mean(liste_utilisateur)))
#             elif choix == 'min':
#                 print("Le minimum est " + str(minimum(liste_utilisateur)))
#             elif choix == 'max':
#                 print("Le maximum est " + str(maximum(liste_utilisateur)))
#             elif choix == 'range':
#                 print("Le range (étendue) est " + str(etendu(liste_utilisateur)))
#             elif choix == 'std':
#                 print("L'écart type est " + str(ecrtype(liste_utilisateur)))
#             elif choix == 'variance':
#                 print("La variance est " + str(calculate_std(liste_utilisateur)))
#             elif choix == 'quartiles':
#                 quartilee(liste_utilisateur)
#             elif choix == 'eqr':
#                 print("Le EQR est " + str(calculate_eqr(liste_utilisateur)))
#             elif choix == 'quit':
#                 break
#             else:
#                 print("Nom de fonction invalide. Veuillez réessayer.")
#
# except ValueError:
#      print("Veuillez entrer un nombre entier.")

