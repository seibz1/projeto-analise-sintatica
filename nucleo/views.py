from django.shortcuts import render
from .models import Periodo  

def home(request):
    """
    Esta View é responsável por buscar todos os períodos cadastrados
    no banco de dados e enviá-los para o template 'home.html'.
    """
    
    # Busca todos os objetos da tabela Periodo
    periodos_cadastrados = Periodo.objects.all()
    
    # Cria o "contexto" para enviar os dados ao template
    context = {
        'lista_periodos': periodos_cadastrados
    }
    
    # Renderiza o HTML (home.html) com os dados (context)
    return render(request, 'home.html', context)