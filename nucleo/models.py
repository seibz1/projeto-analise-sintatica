from django.db import models

# Entidade 1: O Período completo
class Periodo(models.Model):
    """
    Armazena o período completo (simples ou composto) a ser analisado.
    """
    texto_completo = models.TextField("Texto do Período")

    def __str__(self):
        return self.texto_completo[:50] + "..."

    class Meta:
        verbose_name = "Período"
        verbose_name_plural = "Períodos"


# Entidade 2: As Orações dentro do período
class Oracao(models.Model):
    """
    Representa uma oração individual dentro de um Período.
    Inclui o tipo morfológico e a função sintática.
    """
    TIPO_CHOICES = [
        ('PRINCIPAL', 'Oração Principal'),
        ('COORDENADA', 'Coordenada'),
        ('SUB_SUBSTANTIVA', 'Subordinada Substantiva'),
        ('SUB_ADJETIVA', 'Subordinada Adjetiva'),
        ('SUB_ADVERBIAL', 'Subordinada Adverbial'),
    ]

    # Relacionamento hierárquico: Uma Oração pertence a um Período
    periodo = models.ForeignKey(
        Periodo, 
        on_delete=models.CASCADE, 
        related_name="oracoes"
    )
    
    texto_da_oracao = models.CharField("Texto da Oração", max_length=1000)
    
    # Campo para "tipo de oração" (morfológico)
    tipo = models.CharField(
        "Tipo de Oração", 
        max_length=20, 
        choices=TIPO_CHOICES, 
        default='PRINCIPAL'
    )
    
    # Campo para a função sintática da oração (opcional)
    funcao_sintatica = models.CharField(
        "Função Sintática (se subordinada)", 
        max_length=100, 
        blank=True, 
        null=True
    )

    def __str__(self):
        return f"({self.get_tipo_display()}) {self.texto_da_oracao[:40]}..."

    class Meta:
        verbose_name = "Oração"
        verbose_name_plural = "Orações"


# Entidade 3: Componentes essenciais (Sujeito, Predicado)
class ComponenteSintatico(models.Model):
    """
    Catalogar os componentes sintáticos essenciais de cada oração.
    """
    TIPO_COMPONENTE_CHOICES = [
        ('SUJEITO', 'Sujeito'),
        ('PREDICADO', 'Predicado'),
        ('OBJETO_DIRETO', 'Objeto Direto'),
        ('OBJETO_INDIRETO', 'Objeto Indireto'),
        ('COMPLEMENTO_NOMINAL', 'Complemento Nominal'),
        ('ADJUNTO_ADVERBIAL', 'Adjunto Adverbial'),
        ('ADJUNTO_ADNOMINAL', 'Adjunto Adnominal'),
    ]

    # Relacionamento hierárquico: Um Componente pertence a uma Oração
    oracao = models.ForeignKey(
        Oracao, 
        on_delete=models.CASCADE, 
        related_name="componentes"
    )
    
    tipo_componente = models.CharField(
        "Tipo de Componente", 
        max_length=20, 
        choices=TIPO_COMPONENTE_CHOICES
    )
    
    texto_do_componente = models.CharField("Texto do Componente", max_length=500)

    def __str__(self):
        return f"{self.get_tipo_componente_display()}: {self.texto_do_componente}"

    class Meta:
        verbose_name = "Componente Sintático"
        verbose_name_plural = "Componentes Sintáticos"