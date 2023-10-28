# mean$
# median$
# quartile
# variance
# ecart type
# min$
# max$
# EQR
# Etendue$

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
    return