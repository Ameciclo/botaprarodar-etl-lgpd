import unittest
from parameterized import parameterized
from unittest.mock import MagicMock

# CLASSE DE ESTUDO PARA IMPLEMENTAÇÃO DE TESTES UNITÁRIOS EM PYTHON
# ESSA CLASSE NÃO EXECUTA NADA, APENAS PARA REFERÊNCIA 

class PythonTemplateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("up")

    @classmethod
    def tearDownClass(cls):
        print("down")

    def test_bota_pra_rodar_etl(self):
        self.assertTrue(True)

    @parameterized.expand([
        ([1, 2, 3], ),
        ([3, 3], ),
        ([6], ),
    ])
    def test_sums_to_6(self, numbers):
        assert sum(numbers) == 6

    def test_mock(self):
        mock = MagicMock()
        mock.return_value = 1
        assert mock() == 1

        attrs = {'method.return_value': 3, 'withparameter.return_value':3, 'other.side_effect': KeyError}
        mock = MagicMock(some_attribute='eggs', **attrs)
        assert mock.method() == 3   
        mock.method.assert_called_once()

        mock.withparameter(1)
        mock.withparameter.assert_called_once_with(1)

if __name__ == "__main__":
    unittest.main()