# Creare un primo modello. Opzionalmente, realizzare il controllo degli input, sanitizzandoli, ed eseguire dei test. Infine, eseguire commit del file.

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
#           PROGRAMMA
# ==============================
#       Corpo del programma
# ==============================
# Istanziamento di una lista
list = [50, 52, 60]
# Utilizzo del modello predittivo IncrementModel
my_model = IncrementModel()
print('La predizione del modello è: {}'.format(my_model.predict(list)))