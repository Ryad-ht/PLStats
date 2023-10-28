# mean
# median
# quartile
# variance
# ecart type
# min
# max
# EQR
# Etendue

#j'ai cree des variable globale car je voulais reutiliser q1 et q3 qui existe dans ma fonction quartile sans les rentre en parametre dans la fonction eqr
q1 = None
q3 = None
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
    #j'indique que jutiliser des variable globales
    global q1,q3
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
    #il sagit simplement de calculer le q3 moins le q1
    return q3-q1

