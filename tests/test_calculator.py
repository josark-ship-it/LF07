import unittest
# Wir importieren die Funktion aus deinem src-Ordner
from src.calculator import berechne_brutto

class TestMwStRechner(unittest.TestCase):
    
    def test_normalfall_berechnung(self):
        """Testet, ob die Berechnung mit normalen Werten stimmt."""
        self.assertEqual(berechne_brutto(100.0, 19.0), 119.0)
        self.assertEqual(berechne_brutto(10.0, 7.0), 10.7)

    def test_grenzwert_null(self):
        """Grenzwertanalyse: Was passiert, wenn der Preis genau 0 ist?"""
        self.assertEqual(berechne_brutto(0.0, 19.0), 0.0)

    def test_Fehler_bei_negativen_werten(self):
        """Testet, ob das Programm bei ungültigen (negativen) Werten blockiert."""
        with self.assertRaises(ValueError):
            berechne_brutto(-5.0, 19.0)

if __name__ == '__main__':
    unittest.main()