from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Usuario

def exibir_usuarios(request):
    return render(request, 'usuario/index.html')

def usuario_busca(request):
    q = request.GET.get('q', '').strip() #remove espaços em branco no início e no final
    if not q:
        return JsonResponse([], safe=False)

    usuarios = Usuario.objects.filter(first_name__istartswith=q)[:20]

    resultado = []
    for u in usuarios:
        resultado.append({
            'first_name': u.first_name,
            'last_name': u.last_name,
            'email': u.email,
            'city': u.city,
            'thumbnail_url': u.thumbnail_url,
        })

    return JsonResponse(resultado, safe=False)
