from stats.math import *
import random
import csv

data2 = 'data_2 - data_2.csv'

# Ouvrir le fichier en mode lecture
with open(data2, mode='r', encoding='utf-8') as fichier:
    lecteur_data2 = csv.reader(fichier)

    # Parcourir le fichier ligne par ligne
    for ligne in lecteur_data2:
        print(ligne)  # Affiche chaque ligne du fichier CSV

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

