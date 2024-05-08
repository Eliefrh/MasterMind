import unittest
from main import generer_code_secret, evaluer_indice, afficher_points


class TestMastermind(unittest.TestCase):

    def test_longueur_code_secret(self):
        code_secret = generer_code_secret(4)
        self.assertEqual(len(code_secret), 4)

    def test_evaluer_indice(self):
        code_secret = ['R', 'G', 'B', 'Y']
        indice = 'RGBC'
        result = evaluer_indice(code_secret, indice)
        self.assertEqual(result, (indice, ['!', '!', '!']))


if __name__ == '__main__':
    unittest.main()
