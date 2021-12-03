# Scrivere dei test o degli unit test per gli oggetti CSVFile e NumericalCSVFile.

# ==============================
#           CLASSI
# ==============================
#       Classe per CSVFile
# ==============================
class CSVFile():
    
    def __init__(self, name):
        # Istanziamento dell'attributo "name"
        self.name = name
        # Controllo del tipo di nome del file
        if type(name) != str:
            raise TypeError('Errore di tipo: il nome inserito non è una stringa! Ecco il parametro che lo ha generato: {}'.format(name))
    
    def get_data(self, start = None, end = None):
        # Istanziamento di due liste: una lista e una lista di lista
        list = []
        listoflist = []
        # Apertura del file
        try:
            file = open(self.name, 'r')
        except FileNotFoundError:
            print ('Il file che si sta cercando di aprire non esiste!')
        # Controllo della correttezza di start ed end
        if type(start) != int:
            raise TypeError('Errore di tipo: il parametro inserito non è un numero intero!')
        if type(end) != int:
            raise TypeError('Errore di tipo: il parametro inserito non è un numero intero!')
        if(start > len(self.name)):
            raise ValueError('Il file {} ha {} righe'.format(self.name, len(self.name)))
        if(end > len(self.name)):
            raise ValueError('Il file {} ha {} righe'.format(self.name, len(self.name)))
        if(start < 0):
            raise ValueError('Errore di valore: non è accettabile un valore negativo!')
        if(end < 0):
            raise ValueError('Errore di valore: non è accettabile un valore negativo!')
        if(start > end):
            raise ValueError('Il parametro start è maggiore del parametro end')
        # Lettura del file, linea per linea
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
        return listoflist[start : end]
        
# ==============================
#   Classe per NumericalCSVFile
# ==============================
class NumericalCSVFile(CSVFile):

    def get_data(self, start = None, end = None):
        # Richiamo della funzione genitrice
        string_data = super().get_data(start, end)
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
        return numerical_data[start : end]

# ==============================
#           PROGRAMMA
# ==============================
#       Corpo del programma
# ==============================
my_file = CSVFile(name = '../shampoo_sales.csv')
print('Nome del file: {}'.format(my_file.name))
print('Dati contenuti nel file: "{}"'.format(my_file.get_data(5, 8)))

my_numerical_file = NumericalCSVFile(name = '../shampoo_sales.csv')
print('Nome del file numerico: "{}"'.format(my_numerical_file.name))
print('Dati contenuti nel file numerico: "{}"'.format(my_numerical_file.get_data(5, 8)))