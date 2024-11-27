from django.db import models


class Ambiente(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    comprimento = models.FloatField(blank=False)
    largura = models.FloatField(blank=False)
    altura = models.FloatField(blank=False)
    temperatura_interna = models.FloatField(null=True, blank=True)
    temperatura_externa = models.FloatField(null=True, blank=True)
    quantidade_de_lampadas = models.FloatField(null=True, blank=True)
    quantidade_de_pessoas = models.FloatField(null=True, blank=True)
    quantidade_de_eletronicos = models.FloatField(null=True, blank=True)

    def pessoas(self):
        # em media pessoas
        return self.quantidade_de_pessoas * 800

    def lampadas(self):
        # em media de lampadas
        return self.quantidade_de_lampadas * 100

    def eletronicos(self):
        # em media aparelhos eletronicos
        return self.quantidade_de_eletronicos * 1000

    def fluxo_de_calor(self):
        if self.temperatura_interna is None or self.temperatura_externa is None:
            return None
        delta_t = self.temperatura_externa - self.temperatura_interna
        area_total = self.area()
        resistencia_total = self.calcular_resistencia_total()

        if resistencia_total == 0:
            return None

        return area_total * delta_t / resistencia_total

    def fluxo_de_calor_total(self):
        fluxo = self.fluxo_de_calor()
        lampadas = self.lampadas()
        eletronicos = self.eletronicos()
        pessoas = self.pessoas()
        return fluxo + lampadas + eletronicos + pessoas

    def btus(self):
        return self.fluxo_de_calor() * 3.96

    def btus_totais(self):
        return self.fluxo_de_calor_total() * 3.96

    def tamanho(self):
        return self.comprimento * self.largura * self.altura

    def area(self):
        return 2 * (self.comprimento * self.altura + self.largura * self.altura)

    def calcular_resistencia_total(self):
        return sum(camada.calcular_resistencia() for camada in self.camadas.all())

    def __str__(self):
        return self.nome if self.nome else f"Ambiente ({self.id})"


class Camada(models.Model):
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE, related_name="camadas")
    material = models.CharField(max_length=100, blank=False)
    espessura = models.FloatField(blank=False)
    condutividade = models.FloatField(blank=False)

    def __str__(self):
        return f"Camada de {self.material} para o ambiente {self.ambiente.nome}"

    def calcular_metro_quadrado(self):
        return self.comprimento * self.largura

    def calcular_resistencia(self):
        if self.condutividade != 0:
            return self.espessura / self.condutividade
        return 0