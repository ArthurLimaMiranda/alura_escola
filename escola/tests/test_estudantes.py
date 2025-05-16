from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        #self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.usuario = User.objects.get(username='arthurlm')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.get(pk=3)
        self.estudante_02 = Estudante.objects.get(pk=4)

    def test_requisicao_get_para_listar_estudantes(self):
        """
        Teste de requisição GET
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_estudante(self):
        """
        Teste de requisição GET para um estudante
        """
        
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        #print(dados_estudante_serializados)
        self.assertEqual(response.data, dados_estudante_serializados)

    def test_requisicao_post_para_criar_um_estudante(self):
        """
        Teste de requisição POST para um estudante
        """

        dados = {
            'nome': 'Testinho da Silva',
            'email': 'teste@teste.uol',
            'cpf': '82271917034',
            'data_nascimento': '2002-04-02',
            'celular': '99 99999-9999'
        }
        response = self.client.post(self.url,data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_um_estudante(self):
        """
        Teste de requisição DELETE para apagar um estudante
        """
        
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_um_estudante(self):
        """
        Teste de requisição PUT para atualizar um estudante
        """
        
        dados = {
            'nome': 'Testinho da Silva',
            'email': 'teste@teste.uol',
            'cpf': '42370866071',
            'data_nascimento': '2002-04-02',
            'celular': '99 99999-9999'
        }
        response = self.client.put(self.url+'2/',data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)