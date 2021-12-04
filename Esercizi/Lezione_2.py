# Si scriva una funzione che sommi tutti gli elementi di una lista (senza usare la funzione built.in). Poi, eseguire il commit del file.

# ==============================
#           METODI
# ==============================
#             Sum
# ==============================
def sum(list):
    sum = 0
    for number in list:
        sum = sum + number
    print("La somma è: {}".format(sum))
    return sum

# ==============================
#           PROGRAMMA
# ==============================
#       Corpo del programma
# ==============================
# Istanziamento di una lista
list = [1, 2, 3, 4, 5]
# RIchiamo del metodo "sum"
sum(list)