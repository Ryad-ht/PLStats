import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean
from skbio import DistanceMatrix
from skbio.stats.distance import anosim
from statsmodels.multivariate.manova import MANOVA
import scipy.stats as stats
class StatisticalTests:
    def __init__(self, data_dict):
        self.data_dict = data_dict

    def is_categorical(self, key):
        for item in self.data_dict[key]:
            try:
                # Remplacer la virgule par un point et essayer de convertir en float
                # esseyer de supprimer .replace(',', '.') ça devrai marché
                float(item)
            except ValueError:
                # Si la conversion échoue, la variable est catégorielle
                return True
        # Si toutes les conversions réussissent, la variable est quantitative
        return False

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

    def kruskal_wallis_test(self, quantitative_key, qualitative_keys):
        # Création d'un DataFrame pour les analyses
        data = pd.DataFrame({quantitative_key: self.data_dict[quantitative_key]})
        for qual_key in qualitative_keys:
            data[qual_key] = self.data_dict[qual_key]

        # Regrouper les données par les variables qualitatives et calculer les statistiques
        grouped_data = data.groupby(qualitative_keys).agg('mean')  # ou utilisez une autre statistique appropriée

        # Appliquer le test de Kruskal-Wallis sur les groupes
        stat, p_val = stats.kruskal(
            *[group for name, group in grouped_data[quantitative_key].groupby(qualitative_keys)])
        return {'Statistic': stat, 'p-value': p_val}

    def anosim_test(self, quantitative_keys, qualitative_key):
        # Combinaison des variables quantitatives pour créer une matrice de distance
        data_quantitative = pd.DataFrame({key: list(map(float, self.data_dict[key])) for key in quantitative_keys})

        # Assurez-vous que les données sont en format approprié pour le calcul de distance
        # Exemple : utiliser les valeurs sous forme de liste de listes
        quantitative_data_formatted = data_quantitative.values.tolist()

        # Fonction pour calculer la distance euclidienne
        def euclidean_distance(u, v):
            return euclidean(u, v)

        # Création de la matrice de distance
        distance_matrix = DistanceMatrix.from_iterable(quantitative_data_formatted, metric=euclidean_distance)

        # La variable qualitative pour les groupes
        group_data = self.data_dict[qualitative_key]

        # Exécution de ANOSIM
        result = anosim(distance_matrix, group_data)
        return result


    def manova_test(self, dependent_vars, independent_var):
        # 'dependent_vars' est une liste de noms de variables dépendantes
        # 'independent_var' est le nom de la variable indépendante (facteur)
        data = self.data_dict[dependent_vars + [independent_var]]
        manova = MANOVA.from_formula(f'{" + ".join(dependent_vars)} ~ {independent_var}', data)
        return manova.mv_test()

    def check_normality(self, key):
        data = [float(value) for value in self.data_dict[key]]
        stat, p_val = stats.shapiro(data)
        return p_val > 0.05  # Retourne True si p-value > 0.05, indiquant une distribution normale

    def anova_test(self, keys):
        data_groups = [list(map(float, self.data_dict[key])) for key in keys]
        f_stat, p_val = stats.f_oneway(*data_groups)
        return {'F-statistic': f_stat, 'p-value': p_val}
