from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_da_fixtures(self):
        """
        Teste que verifica o carregamento da fixtures
        """
        estudante = Estudante.objects.get(cpf = '17059997865')
        curso = Curso.objects.get(pk=2)

        self.assertEqual(estudante.celular, '26 98135-5153')
        self.assertEqual(curso.codigo, '434')