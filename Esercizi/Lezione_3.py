# Si scriva una funzione che sommi tutti i valori delle vendite degli shampoo del file “shampoo_sales.csv". Poi, eseguire commit del file.

# ==============================
#           METODI
# ==============================
#           Sales
# ==============================
def sales(list):
    sales = 0
    for number in list:
        sales = sales + number
    print("La somma è: {}".format(sales))
    return sales

# ==============================
#           PROGRAMMA
# ==============================
#       Corpo del programma
# ==============================
# Inizializzazione di una lista per salvare i valori
list = []

# Apertura e Lettura del file, linea per linea
my_file = open('shampoo_sales.csv', 'r') 
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

# Richiamo del metodo "sales"
sales(list)