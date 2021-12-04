# Creare un oggetto CSVFile che rappresenti un file CSV, e che: 1. venga inizializzato sul nome del file csv; 2. abbia un attributo “name” che ne contenga il nome; 3. abbia un metodo “get_data()” che torni i dati dal file CSV come lista di liste, ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]. Si provi sul file “shampoo_sales.csv”. Poi, eseguire commit del file.

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
#           PROGRAMMA
# ==============================
#       Corpo del programma
# ==============================
my_file = CSVFile(name = 'shampoo_sales.csv')
print('Nome del file: {}'.format(my_file.name))
print('Dati contenuti nel file: "{}"'.format(my_file.get_data()))