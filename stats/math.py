
import numpy as np
from scipy.stats import shapiro, ttest_1samp, ttest_ind, wilcoxon, kruskal

def print_mean_definition():
    print("\nMoyenne : La moyenne est la somme des valeurs divisée par le nombre de valeurs.")

def calculate_mean(numbers):
    print_mean_definition()
    mean = sum(numbers) / len(numbers)
    return mean

def print_median_definition():
    print("\nMédiane : La valeur qui sépare la moitié supérieure de la moitié inférieure des données.")

def calculate_median(numbers):
    print_median_definition()
    if not numbers:
        return None

    numbers.sort()
    n = len(numbers)
    middle = n // 2

    if n % 2 == 1:
        return numbers[middle]
    else:
        return (numbers[middle - 1] + numbers[middle]) / 2

def print_min_max_definition():
    print("\nMinimum et Maximum : Les plus petites et les plus grandes valeurs dans l'ensemble des données.")

def find_minimum(numbers):
    print_min_max_definition()
    min_value = min(numbers)
    return min_value

def find_maximum(numbers):
    print_min_max_definition()
    max_value = max(numbers)
    return max_value

def print_range_definition():
    print("\nÉtendue : La différence entre la valeur maximale et la valeur minimale.")

def calculate_range(numbers):
    print_range_definition()
    return find_maximum(numbers) - find_minimum(numbers)

def print_variance_definition():
    print("\nVariance : Mesure la dispersion des données autour de la moyenne.")

def calculate_variance(numbers):
    print_variance_definition()
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance

def print_std_dev_definition():
    print("\nÉcart-type : Racine carrée de la variance, mesure la dispersion des données.")

def calculate_std_dev(numbers):
    print_std_dev_definition()
    variance = calculate_variance(numbers)
    std_dev = variance ** 0.5
    return std_dev

def print_quartiles_definition():
    print("\nQuartiles : Divisent l'ensemble des données en quatre parties égales.")

def calculate_quartiles(numbers):
    print_quartiles_definition()
    numbers.sort()
    q2 = calculate_median(numbers)
    lower_half = [x for x in numbers if x < q2]
    upper_half = [x for x in numbers if x > q2]
    q1 = calculate_median(lower_half)
    q3 = calculate_median(upper_half)
    result = f"Q1: {q1}, \nQ2 (Median): {q2}, \nQ3: {q3}"
    print(result)
    return result

def print_iqr_definition():
    print("\nIntervalle interquartile (IQR) : La différence entre le troisième et le premier quartile.")

def calculate_iqr(numbers):
    print_iqr_definition()
    numbers.sort()
    q2 = calculate_median(numbers)
    lower_half = [x for x in numbers if x < q2]
    upper_half = [x for x in numbers if x > q2]
    q1 = calculate_median(lower_half)
    q3 = calculate_median(upper_half)
    return q3 - q1


def explication_shapiro_wilk():
    print("\nExplication: Test de Shapiro-Wilk")
    print("Ce test vérifie si un échantillon provient d'une population normalement distribuée.")

def effectuer_shapiro_wilk(donnees):
    stat, p = shapiro(donnees)
    print(f"Shapiro-Wilk Statistique={stat}, p-value={p}")
    return p > 0.05  # Retourne True si les données semblent normales, False sinon


