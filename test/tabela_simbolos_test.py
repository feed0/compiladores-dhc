import unittest
from tabela_simbolos import TabelaDeSimbolos

class TestTabelaDeSimbolos(unittest.TestCase):
    def setUp(self):
        # Configuração inicial antes de cada teste
        self.tabela = TabelaDeSimbolos()

    def test_inserir_e_buscar_simbolo(self):
        self.tabela.inserir("x", "int", 10)
        simbolo = self.tabela.buscar("x")
        self.assertIsNotNone(simbolo)
        self.assertEqual(simbolo["tipo"], "int")
        self.assertEqual(simbolo["valor"], 10)

    def test_inserir_simbolo_existente(self):
        self.tabela.inserir("x", "int", 10)
        with self.assertRaises(KeyError):
            self.tabela.inserir("x", "int", 20)

    def test_atualizar_simbolo(self):
        self.tabela.inserir("x", "int", 10)
        self.tabela.atualizar("x", 20)
        simbolo = self.tabela.buscar("x")
        self.assertEqual(simbolo["valor"], 20)

    def test_atualizar_simbolo_inexistente(self):
        with self.assertRaises(KeyError):
            self.tabela.atualizar("x", 20)

    def test_remover_simbolo(self):
        self.tabela.inserir("x", "int", 10)
        self.tabela.remover("x")
        simbolo = self.tabela.buscar("x")
        self.assertIsNone(simbolo)

    def test_remover_simbolo_inexistente(self):
        with self.assertRaises(KeyError):
            self.tabela.remover("x")

    def test_exibir_tabela(self):
        self.tabela.inserir("x", "int", 10)
        self.tabela.inserir("y", "float", 20.5)
        self.tabela.inserir("z", "string", "Olá")
        # Apenas verificando se o método exibir não gera erros
        self.tabela.exibir()

if __name__ == "__main__":
    unittest.main()