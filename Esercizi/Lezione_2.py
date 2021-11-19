# Si scriva una funzione che sommi tutti gli elementi di una lista (senza usare la funzione built.in). Poi, eseguire il commit del file.

# --- FUNZIONI ---
#
# Funzione "Somma"
def somma(lista):
    risultato = 0
    for numero in lista:
        risultato = risultato + numero
    return print("Somma: {}".format(risultato))

# --- PROGRAMMA PRINCIPALE ---
lista = [1, 2, 3, 4, 5]
somma(lista)