# Scrivere dei test o degli unit test per gli oggetti CSVFile e NumericalCSVFile.

# ==============================
#           CLASSI
# ==============================
#       Classe per CSVFile
# ==============================
import unittest
from Lezione_7 import CSVFile

# Testing
class TestCSVFile(unittest.TestCase):

    def test_init(self):
        # Istanziamento dell'attributo "name"
        csv_file = CSVFile('../shampoo_sales.csv')
        # Controllo del salvataggio del nome del file come attributo "name" dell’oggetto
        self.assertEqual(csv_file.name, '../shampoo_sales.csv')