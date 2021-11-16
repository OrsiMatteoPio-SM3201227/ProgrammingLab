#Scrivere una funzione che sommi tutti gli elementi di una lista (senza usare la funzione built.in)

def somma(lista): #Definizione della funzione somma
  risultato=0
  for numero in lista: #Calcolo del risultato
    risultato=risultato+numero
  return print("Somma: {}".format(risultato)) #Stampa del risultato

lista=[1, 2, 3, 4, 5] #Definizione della lista
somma(lista) #Richiamo della funzione somma