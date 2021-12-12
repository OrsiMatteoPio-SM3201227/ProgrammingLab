# Estendere il modello della lezione precedente IncrementModel come FitIncrementModel, andando ad implementare il metodo fit(). Il fit deve, come appena descritto, calcolare l’incremento medio su tutto il dataset e salvarlo da qualche parte (es: self.global_avg_increment). Poi, sovrascrivere il metodo predict() in modo che usi l’incremento medio su tutto il dataset come descritto nelle slides precedenti. Infine, eseguire il commit del file.

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
        increment = 0
        # Aggiornamento dell'incremento mediante un ciclo, passando per il terzultimo e il penultimo valore della lista
        for i in range(-3, -1):
            if(data[i] > data[i+1]):
                increment = increment + (data[i] - data[i+1])
            else:
                increment = increment + (data[i+1] - data[i])
        # Divisione dell'incremento per 2
        increment = increment/2
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
        # Istanziamento della variabile predizione mediante la somma dell'ultimo elemento della lista e l'(.self)incremento
        prediction = data[-1] + self.global_avg_increment
        return prediction

# ==============================
#           PROGRAMMA
# ==============================
#       Corpo del programma
# ==============================
# Istanziamento di una lista
data = [8,19,31,41,50,52,60]
# Utilizzo del modello predittivo FitIncrementModel
my_model = FitIncrementModel()
print('Incremento medio: {}'.format(my_model.fit(data)))
print('La predizione del modello è: {}'.format(my_model.predict(data)))
# Visualizzazione grafica di dati e predizione
from matplotlib import pyplot
pyplot.plot(data + [my_model.predict(data)], color = 'tab:red')
pyplot.plot(data, color = 'tab:blue')
pyplot.show()