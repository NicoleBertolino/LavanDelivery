from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from .models import PacoteRepublica, Plano


class ListaPlanosTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Plano.objects.create(
            nome="Padrão", kg_mes=20, preco="99.00", coletas_semana=1,
            prazo="24–48h", destaque=True,
        )
        Plano.objects.create(
            nome="Básico", kg_mes=12, preco="69.00", coletas_semana=1,
            prazo="48h", beneficios="≈ 3 lavagens de 4 kg",
        )
        PacoteRepublica.objects.create(
            pessoas=12, kg_semana=45, preco_morador="42.00", ciclos=3,
            coletas_semana=1, destaque=True,
        )

    def test_mostra_planos_e_pacotes(self):
        resposta = self.client.get(reverse("planos"))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Básico")
        self.assertContains(resposta, "≈ 3 lavagens de 4 kg")
        self.assertContains(resposta, "12 pessoas")
        self.assertContains(resposta, "Mais escolhido")
        self.assertContains(resposta, "Mais comum")

    def test_planos_ordenados_por_preco(self):
        resposta = self.client.get(reverse("planos"))
        nomes = [p.nome for p in resposta.context["planos"]]
        self.assertEqual(nomes, ["Básico", "Padrão"])

    def test_aba_padrao_e_individual(self):
        resposta = self.client.get(reverse("planos"))
        self.assertEqual(resposta.context["aba"], "individual")

    def test_aba_republica_pela_url(self):
        resposta = self.client.get(reverse("planos"), {"aba": "republica"})
        self.assertEqual(resposta.context["aba"], "republica")

    def test_aba_invalida_volta_para_individual(self):
        resposta = self.client.get(reverse("planos"), {"aba": "qualquer"})
        self.assertEqual(resposta.context["aba"], "individual")


class FixtureTests(TestCase):
    def test_fixture_carrega_os_dados_do_prototipo(self):
        call_command("loaddata", "planos", verbosity=0)
        self.assertEqual(Plano.objects.count(), 3)
        self.assertEqual(PacoteRepublica.objects.count(), 4)
        self.assertEqual(Plano.objects.filter(destaque=True).get().nome, "Padrão")
