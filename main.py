# Importation des modules nécessaires
import csv
from stats import StatisticalTests  # Assurez-vous que cette classe existe dans votre module stats

# Chemin vers le fichier de données
data2 = 'data_2 - data_2.csv'

# Lecture des données à partir du fichier CSV et stockage dans un dictionnaire
donnees_dict = {}
with open(data2, mode='r', encoding='utf-8') as fichier:
    lecteur_data2 = csv.DictReader(fichier)
    for ligne in lecteur_data2:
        for cle, valeur in ligne.items():
            # Remplacer la virgule par un point dans les valeurs
            valeur_modifiee = valeur.replace(',', '.')
            if cle not in donnees_dict:
                donnees_dict[cle] = []
            donnees_dict[cle].append(valeur_modifiee)

# Affichage des clés disponibles dans le dictionnaire pour que l'utilisateur puisse choisir
print("Voici les clés disponibles :")
for cle in donnees_dict.keys():
    print(cle)

# Demander à l'utilisateur d'entrer les clés des données à analyser
cle_utilisateur = input("Entrez les clés des données que vous souhaitez analyser (séparées par une virgule) : ")
cles_choisies = [cle.strip() for cle in cle_utilisateur.split(',')]  # Nettoie les espaces avant et après les entrées

# Création d'une instance de la classe StatisticalTests
tests_statistiques = StatisticalTests(donnees_dict)

# Fonction principale pour déterminer quel test statistique effectuer
def determiner_et_effectuer_test(cles):
    for cle in cles:
        if cle not in donnees_dict:
            print(f"La clé '{cle}' n'a pas été trouvée. Veuillez vérifier votre saisie.")
            return

    print(f"Clés sélectionnées pour le test : {cles}")
    types = [tests_statistiques.is_categorical(cle) for cle in cles]

    # Cas où il y a mélange de variables quantitatives et qualitatives
    if any(types) and not all(types):
        cles_quantitatives = [cle for cle, is_cat in zip(cles, types) if not is_cat]
        cles_qualitatives = [cle for cle, is_cat in zip(cles, types) if is_cat]

        # Si une seule variable quantitative et une ou plusieurs variables qualitatives
        if len(cles_quantitatives) == 1 and len(cles_qualitatives) >= 1:
            is_normal = tests_statistiques.check_normality(cles_quantitatives[0])

            if is_normal:
                print(f"Effectuer une ANOVA pour les variables : {cles}.")
                result = tests_statistiques.anova_test(cles)
            else:
                print(f"Effectuer un Kruskal-Wallis pour les variables : {cles}.")
                result = tests_statistiques.kruskal_wallis_test(cles)
        # Autres cas
        else:
            print("Effectuer un test approprié pour les variables sélectionnées.")
            result = None
    else:
        print("Veuillez sélectionner une combinaison appropriée de variables qualitatives et quantitatives.")
        result = None

    print("Résultat du test statistique :")
    print(result)

# Exécution du test statistique
determiner_et_effectuer_test(cles_choisies)
