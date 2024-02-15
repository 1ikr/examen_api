from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Socio
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def introducir_socio(request):
    if request.method == 'POST':
        data = request.POST
        dni = data.get('dni')
        numero_socio = data.get('numero_socio')
        contraseña = data.get('contraseña')
        socio = Socio.objects.create(dni=dni, numero_socio=numero_socio, contraseña=contraseña)
        return JsonResponse({'message': 'Socio añadido correctamente'}, status=201)

@csrf_exempt
def modificar_contraseña(request, numero_socio):
    socio = get_object_or_404(Socio, numero_socio=numero_socio)
    if request.method == 'POST':
        data = request.POST
        nueva_contraseña = data.get('nueva_contraseña')
        socio.contraseña = nueva_contraseña
        socio.save()
        return JsonResponse({'message': 'Contraseña modificada correctamente'}, status=200)

@csrf_exempt
def obtener_todos_socios(request):
    socios = Socio.objects.all()
    data = [{'dni': socio.dni, 'numero_socio': socio.numero_socio, 'contraseña': socio.contraseña} for socio in socios]
    return JsonResponse(data, safe=False)
