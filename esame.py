# Esercitazione 2.

# ==============================
#           CLASSI
# ==============================
#    Classe per ExamException
# ==============================
class ExamException(Exception):
    pass
# ==============================
#       Classe per Diff
# ==============================
class Diff():
    
    def __init__(self):
        # Istanziamento dell'attributo opzionale "ratio"
        self.ratio = 1
    
    def compute(self, data):
        # Istanziamento di una lista
        differences = []
        # Calcolo della differenza
        for number in range(len(data) - 1):
            differences.append(abs(data[number] - data[number + 1]) / self.ratio)
        return differences

# ==============================
#           PROGRAMMA
# ==============================
#       Corpo del programma
# ==============================
diff = Diff()

diff.ratio = 1

result = diff.compute([2, 4, 8, 16])

print(result)