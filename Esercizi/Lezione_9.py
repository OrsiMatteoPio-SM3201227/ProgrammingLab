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
# Istanziamento di una lista
data = [8, 19, 31, 41, 50, 52, 60]
fit_data = [8, 19, 31, 41]
predict_data = [50, 52, 60]

# Utilizzo del modello predittivo IncrementModel
my_model = IncrementModel()
print('La predizione del modello IncrementModel è: {}'.format(my_model.predict(predict_data)))

# Utilizzo del modello predittivo FitIncrementModel
my_fit_model = FitIncrementModel()
print('Incremento medio: {}'.format(my_fit_model.fit(fit_data)))
print('La predizione del modello FitIncrementModel è: {}'.format(my_fit_model.predict(predict_data)))