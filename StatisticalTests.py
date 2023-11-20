import numpy as np
import scipy.stats as stats


class StatisticalTests:
    def __init__(self, data_dict):
        self.data_dict = data_dict

    def is_categorical(self, key):
        # Cette fonction vérifie si les données sous la clé sont catégorielles
        # en vérifiant si elles sont de type string (une méthode simple, peut nécessiter une logique plus complexe)
        return all(isinstance(item, str) for item in self.data_dict[key])

    def count_modalities(self, key):
        # Cette fonction compte le nombre de modalités uniques pour une clé donnée
        return len(set(self.data_dict[key]))

    def wilcoxon_signed_rank_test(self, keys):
        # Test de Wilcoxon pour des échantillons appariés
        # Convertir les données en numérique
        data1 = list(map(float, self.data_dict[keys[0]]))
        data2 = list(map(float, self.data_dict[keys[1]]))
        # Effectuer le test de Wilcoxon
        stat, p = stats.wilcoxon(data1, data2)
        return {'statistic': stat, 'p-value': p}

    def kruskal_wallis_test(self, keys):
        # Test de Kruskal-Wallis pour une ou plusieurs variables catégorielles
        # Convertir les données en numérique
        data = [list(map(float, self.data_dict[key])) for key in keys]
        # Effectuer le test de Kruskal-Wallis
        stat, p = stats.kruskal(*data)
        return {'statistic': stat, 'p-value': p}

    def anosim_test(self, keys):
        # ANOSIM pour des groupes catégoriels
        # Cette méthode est un placeholder, ANOSIM n'est pas directement disponible dans scipy
        # Vous devrez utiliser une bibliothèque comme 'skbio.stats.distance' pour ANOSIM
        # Ou implémenter le test vous-même
        pass

    def manova_test(self, keys):
        # MANOVA pour plusieurs variables quantitatives
        # Cette méthode est un placeholder, MANOVA nécessite l'utilisation de 'statsmodels'
        # Vous devrez construire le modèle et effectuer le test en utilisant 'statsmodels.multivariate.manova.MANOVA'
        pass

# Exemple d'utilisation :
# stats_tests = StatisticalTests(donnees_dict)
# result = stats_tests.wilcoxon_signed_rank_test(['key1', 'key2'])
# print(result)
