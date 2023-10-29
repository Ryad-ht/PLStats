# mean
# median
# quartile
# variance
# ecart type
# min
# max
# EQR
# Etendue

def calculate_mean(numbers):
    mean = sum(numbers) / len(numbers)
    return mean
def median(numbers):
    #verifier que la liste n'est pas vide
    if not numbers:
        return None

    #trier la liste
    numbers.sort()

    n = len(numbers)
    middle = n // 2

    if n % 2 == 1:
        return numbers[middle]
    else :
        return (numbers[middle -1] + numbers[middle])/2
def minimum(numbers):
    #recupere le premier elem
    i = 0
    min = numbers[i]
    #comparer et remplacer par le plus petit elem
    for i in range(1, len(numbers)):
        if(numbers[i]<min):
            min = numbers[i]
    return min
def maximum(numbers):
    # recupere le premier elem
    i = 0
    max = numbers[i]
    # comparer et remplacer par le plus grand elem
    for i in range(1, len(numbers)):
        if (numbers[i] > max):
            max = numbers[i]
    return max
def etendu(numbers):
    return maximum(numbers)-minimum(numbers)
def ecrtype(numbers):
    ecrtyp = sum((x - calculate_mean(numbers))**2 for x in numbers)/(len(numbers))
    return ecrtyp
def calculate_std(numbers):
    return etendu(numbers)**2


def quartilee(numbers):
    # les quartile sont des medians de median alors nous allon fonctionner ansi
    numbers.sort()
    q2 = median(numbers)
    lower_half = [x for i,x in enumerate(numbers) if i< len(numbers)/2]
    upper_half = [x for i,x in enumerate(numbers) if i>=len(numbers)/2]
    q1 = median(lower_half)
    q3 = median(upper_half)
    result = f"Q1: {q1}, \nQ2 (Median): {q2}, \nQ3: {q3}"
    print(result)
    return result


def calculate_eqr(numbers):
    numbers.sort()
    q2 = median(numbers)
    lower_half = [x for i, x in enumerate(numbers) if i < len(numbers) / 2]
    upper_half = [x for i, x in enumerate(numbers) if i >= len(numbers) / 2]
    q1 = median(lower_half)
    q3 = median(upper_half)
    return q3-q1

def shapiro_wilk(numbers):
    # trier les donner en ordre croissant et recuper la taille de lechantillion
    numbers.sort()
    n=len(numbers)
