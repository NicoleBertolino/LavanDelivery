from django.db import models


class Plano(models.Model):
    """Assinatura mensal individual."""

    nome = models.CharField(max_length=60)
    kg_mes = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    coletas_semana = models.PositiveSmallIntegerField(default=1)
    prazo = models.CharField(max_length=40)
    beneficios = models.TextField(blank=True, help_text="Um benefício por linha.")
    destaque = models.BooleanField(default=False)

    class Meta:
        ordering = ["preco"]

    def __str__(self):
        return self.nome

    @property
    def lista_beneficios(self):
        return [linha.strip() for linha in self.beneficios.splitlines() if linha.strip()]


class PacoteRepublica(models.Model):
    """Pacote semanal para repúblicas (preço por morador)."""

    pessoas = models.PositiveSmallIntegerField()
    kg_semana = models.PositiveIntegerField()
    preco_morador = models.DecimalField(max_digits=6, decimal_places=2)
    ciclos = models.PositiveSmallIntegerField()
    coletas_semana = models.PositiveSmallIntegerField(default=1)
    destaque = models.BooleanField(default=False)

    class Meta:
        ordering = ["pessoas"]
        verbose_name = "pacote de república"
        verbose_name_plural = "pacotes de república"

    def __str__(self):
        return f"Pacote para {self.pessoas} pessoas"
