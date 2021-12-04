# Parte 1 - Modificare l’oggetto CSVFile della lezione precedente in modo che stampi a schermo un messaggio di errore se si cerca di aprire un file non esistente.
# Parte 2 - Estendere l’oggetto CSVFile chiamandolo NumericalCSVFile e facendo in modo che converta automaticamente a numero tutte le colonne tranne la prima (della data). Poi, aggiungere questi due campi al file “shampoo_sales.csv”: (*Vedere slide*). Quindi, gestire gli errori che verranno generati in modo che le linee vengano saltate senza bloccare il programma ma che venga stampato a schermo l’errore. Infine, eseguire commit del file.

# ==============================
#           CLASSI
# ==============================
#       Classe per CSVFile
# ==============================
class CSVFile():
    
    def __init__(self, name):
        # Istanziamento dell'attributo "name"
        self.name = name
    
    def get_data(self):
        # Istanziamento di due liste: una lista e una lista di lista
        list = []
        listoflist = []
        # Apertura e Lettura del file, linea per linea
        try:
            file = open(self.name, 'r')
        except FileNotFoundError:
            print ('Il file che si sta cercando di aprire non esiste!')
            return None
        for line in file:
            # Istanziamento di elementi con split di ogni riga su ","
            elements = line.split(',')
            # Eliminazione di caratteri indesiderati (newline e spazi)
            elements[-1] = elements[-1].strip()
            # Se non si processa l'intestazione, aggiunta degli elementi alla lista
            if elements[0] != 'Date':
                list.append(elements)
        # Chiusura del file
        file.close()
        # Aggiunta degli elementi della lista alla lista di lista
        listoflist.extend(list)
        return listoflist

# ==============================
#   Classe per NumericalCSVFile
# ==============================
class NumericalCSVFile(CSVFile):

    def get_data(self):
        # Richiamo del metodo genitore
        string_data = super().get_data()
        # Istanziamento di una lista per salvare i valori
        numerical_data = []
        # Lettura del file, linea per linea
        for string_row in string_data:
            numerical_row = []
            for i, element in enumerate(string_row):
                if i == 0:
                    numerical_data.append(element)
                else:
                    try:
                        numerical_data.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
                if len(numerical_row) == len(string_row):
                    numerical_data.append(numerical_row)
        return numerical_data

# ==============================
#           PROGRAMMA
# ==============================
#       Corpo del programma
# ==============================
my_file = CSVFile(name = 'shampoo_sales.csv')
print('Nome del file: {}'.format(my_file.name))
print('Dati contenuti nel file: "{}"'.format(my_file.get_data()))

my_numerical_file = NumericalCSVFile(name = 'shampoo_sales.csv')
print('Nome del file numerico: "{}"'.format(my_numerical_file.name))
print('Dati contenuti nel file numerico: "{}"'.format(my_numerical_file.get_data()))