from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
                nome = 'Testinho da Silva',
                email = 'testedemodelo@gmail.com',
                cpf = '68195899056',
                data_nascimento = '2023-02-02',
                celular = '86 99999-9999'
        )


    def test_verifica_atributos_de_estudante(self):
        """Teste que verifica os atributos do modelo de Estudante"""
        self.assertEqual(self.estudante.nome,'Testinho da Silva')
        self.assertEqual(self.estudante.email,'testedemodelo@gmail.com')
        self.assertEqual(self.estudante.cpf,'68195899056')
        self.assertEqual(self.estudante.data_nascimento,'2023-02-02')
        self.assertEqual(self.estudante.celular,'86 99999-9999')

class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create (
            codigo = 'ABC',
            descricao = 'Teste de texto para uma descrição',
            nivel = 'A'
        )

    def test_verifica_atributos_de_curso(self):
        """Teste que verifica os atributos do modelo de curso"""
        self.assertEqual(self.curso.codigo,'ABC' )
        self.assertEqual(self.curso.descricao, 'Teste de texto para uma descrição')
        self.assertEqual(self.curso.nivel, 'A')

class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
                nome = 'Testinho da Silva',
                email = 'testedemodelo@gmail.com',
                cpf = '68195899056',
                data_nascimento = '2023-02-02',
                celular = '86 99999-9999'
        )

        self.curso = Curso.objects.create (
            codigo = 'ABC',
            descricao = 'Teste de texto para uma descrição',
            nivel = 'A'
        )

        self.matricula = Matricula.objects.create(
            estudante = self.estudante,
            curso = self.curso,
            periodo = 'Matutino'
        )

    def test_verifica_atributos_de_matricula(self):
        """Teste que verifica os atributos do modelo de matricula"""
        self.assertEqual(self.matricula.estudante, self.estudante)
        self.assertEqual(self.matricula.curso, self.curso)
        self.assertEqual(self.matricula.periodo, 'Matutino')
