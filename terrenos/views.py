from django.shortcuts import render, redirect
from .models import Terreno
from usuarios.models import Caficultor
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def mis_terrenos(request):
    if request.user.usuario.tipo_usuario == 'Caficultor':
        # Usuario tipo 'Caficultor' solo puede ver sus propios terrenos
        terrenos = Terreno.objects.filter(caficultor=request.user.usuario.caficultor)
        context = {
            'terrenos': terrenos
        }
    elif request.user.usuario.tipo_usuario == 'AdminCoffeeWeb':
        # Usuario tipo 'AdminCoffeeWeb' ve todos los terrenos agrupados por caficultor
        terrenos_por_caficultor = {}
        caficultores = Caficultor.objects.all()
        for caficultor in caficultores:
            terrenos_por_caficultor[caficultor] = Terreno.objects.filter(caficultor=caficultor)
        context = {
            'terrenos_por_caficultor': terrenos_por_caficultor
        }
    else:
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

    return render(request, 'mis_terrenos.html', context)

@login_required
def crear_terreno(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        departamento = request.POST['departamento']
        ciudad = request.POST['ciudad']
        barrio = request.POST['barrio']
        tipo_calle = request.POST['tipo-calle']
        calle = request.POST['calle']
        numero1 = request.POST['numero1']
        numero2 = request.POST['numero2']
        area = request.POST['area']
        nivelacion = request.POST['nivelacion']
        tipo_suelo = request.POST['tipo-suelo']
        altitud = request.POST['altitud']

        caficultor = request.user.usuario.caficultor

        terreno = Terreno(
            nombre=nombre,
            departamento=departamento,
            ciudad=ciudad,
            barrio=barrio,
            tipo_calle=tipo_calle,
            calle=calle,
            numero1=numero1,
            numero2=numero2,
            area=area,
            nivelacion=nivelacion,
            tipo_suelo=tipo_suelo,
            altitud=altitud,
            caficultor=caficultor
        )
        terreno.save()
        return redirect('mis_terrenos')
    return render(request, 'crear_terreno.html')

@login_required
def editar_terreno(request, terreno_id):
    terreno = get_object_or_404(Terreno, id=terreno_id, caficultor=request.user.usuario.caficultor)
    if request.method == 'POST':
        terreno.nombre = request.POST['nombre']
        terreno.departamento = request.POST['departamento']
        terreno.ciudad = request.POST['ciudad']
        terreno.barrio = request.POST['barrio']
        terreno.tipo_calle = request.POST['tipo-calle']
        terreno.calle = request.POST['calle']
        terreno.numero1 = request.POST['numero1']
        terreno.numero2 = request.POST['numero2']
        terreno.area = request.POST['area']
        terreno.nivelacion = request.POST['nivelacion']
        terreno.tipo_suelo = request.POST['tipo-suelo']
        terreno.save()
        return redirect('mis_terrenos')
    return render(request, 'editar_terreno.html', {'terreno': terreno})

@login_required
def eliminar_terreno(request, terreno_id):
    if request.method == 'DELETE':
        terreno = get_object_or_404(Terreno, id=terreno_id, caficultor=request.user.usuario.caficultor)
        terreno.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)