# Valutare i due modelli delle lezioni 8 e 9, ovvero quello senza fit (IncrementModel) e quelo con fit (IncrementModel) sui dati delle vendite degli shampoo. Per valutarli, occorre: 1. dividere il dataset delle vendite degli shampoo in 24 mesi di dati di fit (che non serviranno per il modello senza fit) e in 12 mesi di dati (gli ultimi) da usare per la valutazione; 2. applicare i modelli sui dati di valutazione confrontando le predizioni con i valori veri. Infine, eseguire il commit del file.

# ==============================
#           METODI
# ==============================
#       Average Increment
# ==============================
def average_increment(data):
    # Istanziamento della variabile di incremento
    avg_increment = 0
    # Aggiornamento dell'incremento mediante un ciclo, passando per tutti i valori della lista fino al penultimo
    for i in range(len(data)-1):
            if(data[i] > data[i+1]):
                avg_increment = avg_increment + (data[i] - data[i+1])
            else:
                avg_increment = avg_increment + (data[i+1] - data[i])
    # Divisione dell'incremento per la lunghezza della lista escluso l'ultimo suo valore
    avg_increment = avg_increment/(len(data)-1)
    return avg_increment

# ==============================
#           CLASSI
# ==============================
#   Classe generica per Model
# ==============================
class Model():

    def fit(self, data):
        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        # Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

# ==============================
#   Classe per IncrementModel
# ==============================
class IncrementModel(Model):

    def fit(self, data):
        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        # Istanziamento della variabile predizione e della variabile di incremento
        prediction = 0
        increment = average_increment(data)
        # Aggiornamento della predizione mediante la somma dell'ultimo elemento della lista e l'incremento
        prediction = data[-1] + increment
        return prediction

# ==============================
#   Classe per FitIncrementModel
# ==============================
class FitIncrementModel(IncrementModel):

    def fit(self, data):
        # Istanziamento della variabile (.self)incremento, aggiornata mediante il metodo che calcola l'incremento
        self.global_avg_increment = average_increment(data)
        return self.global_avg_increment
        
    def predict(self, data):
        # Istanziamento della variabile che raccoglie la predizione della classe genitrice, della variabile che raccoglie l'incremento medio della predizione della classe genitrice e della variabile di incremento medio della prossima predizione
        parent_prediction = super().predict(data)
        parent_predict_increment = parent_prediction - data[-1]
        predict_increment = (self.global_avg_increment + parent_predict_increment) / 2
        # Istanziamento della variabile predizione mediante la somma dell'ultimo elemento della lista e l'(.self)incremento
        prediction = data[-1] + predict_increment
        return prediction

# ==============================
#           PROGRAMMA
# ==============================
#       Corpo del programma
# ==============================
# Istanziamento di una lista di tutti i mesi del file
dataset = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]

fit_dataset = len(dataset) - 12
evaluation_dataset = len(dataset) 

# Utilizzo del modello predittivo IncrementModel
my_model = IncrementModel()
print('La predizione del modello IncrementModel è: {}'.format(my_model.predict(dataset_36mesi)))

# Utilizzo del modello predittivo FitIncrementModel
my_fit_model = FitIncrementModel()
print('Incremento medio: {}'.format(my_fit_model.fit(dataset_36mesi)))
print('La predizione del modello FitIncrementModel è: {}'.format(my_fit_model.predict(dataset_36mesi)))