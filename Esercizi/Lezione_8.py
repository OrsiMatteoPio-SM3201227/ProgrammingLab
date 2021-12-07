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
        # Istanziamento della variabile predizione e della variabile di differenza
        prediction = 0
        increment = 0
        for i in range(len(data)-1):
            if(data[i] > data[i+1]):
                increment = increment + (data[i] - data[i+1])
            else:
                increment = increment + (data[i+1] - data[i])
        prediction = increment/(len(data)-1) + data[-1]
        return prediction

# ==============================
#           PROGRAMMA
# ==============================
#       Corpo del programma
# ==============================
# Istanziamento di una lista
list = [50, 52, 60]
# Utilizzo il modello predittivo
my_model = IncrementModel()
print('La predizione del modello è: {}'.format(my_model.predict(list)))