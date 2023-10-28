from stats.math import *

quanti = [ 32 , -2 , 3 , 4 , -5 , 6 ]
quali = [ 'B' , 'B' , 'B' , 'Y' , 'Y' , 'B' , 'Y' ]


# Dans main.py
print("la moyen est "+str(calculate_mean(quanti)))

print("la median est "+str(median(quanti)))

print("le minimum est "+str(minimum(quanti)))

print("le maximum est "+str(maximum(quanti)))

print("le range(etendu) est "+str(etendu(quanti)))

print("l'ecart type est "+str(ecrtype(quanti)))

print("la variance est "+str(calculate_std(quanti)))