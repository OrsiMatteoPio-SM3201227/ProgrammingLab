# Si scriva una funzione che sommi tutti i valori delle vendite degli shampoo del file “shampoo_sales.txt". Poi, eseguire commit del file.

# --- FUNZIONI ---
#
# Funzione Sales
def sales(list):
    sum = 0
    for number in list:
        sum = sum + number
    return print("La somma è: {}".format(sum))

# --- PROGRAMMA PRINCIPALE ---
#
# Inizializzazione di una lista per salvare i valori
list = []

# Apertura e Lettura del file, linea per linea
my_file = open("shampoo_sales.txt", "r") 
for line in my_file:
    # Split di ogni riga su ","
    elements = line.split(",");
    # Esclusione dell'intestazione
    if elements[0] != "Date":
        # Salvataggio di date e valori
        date = elements[0]
        value = elements[1]
        # Aggiunta dei valori alla lista
        list.append(float(value))

# Richiamo della funzione Sales
sales(list)