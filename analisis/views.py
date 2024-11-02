from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from terrenos.models import Terreno
from usuarios.models import Caficultor, Usuario
from .models import ResultadoEvaluacion
import datetime
from django.http import JsonResponse

# Create your views here.
@login_required
def cultivo (request):
    try:
        caficultor = request.user.usuario.caficultor
    except Caficultor.DoesNotExist:
        # Manejar caso donde el usuario no tiene un caficultor asociado
        return HttpResponse("No se encontró un caficultor asociado para este usuario.")

    # Filtra los terrenos por el caficultor del usuario actual
    terrenos = Terreno.objects.filter(caficultor=caficultor)
    context = {
        'terrenos': terrenos,
    }
    return render(request, 'cultivo.html', context)

@login_required
def evaluar_cultivo(request):
    if request.method == 'POST':
        altitud = request.POST['altitud']
        area_cultivada = request.POST['area_cultivada']
        variedad_cafe = request.POST['variedad_cafe']
        edad_cultivo = request.POST['edad_cultivo']
        densidad_plantacion = request.POST['densidad_plantacion']
        sistema_cultivo = request.POST['sistema_cultivo']
        date_ultima_cosecha = request.POST['date_ultima_cosecha']
        produccion_anual = request.POST['produccion_anual']
        tipo_riego = request.POST['tipo_riego']
        fertilizantes = request.POST['fertilizantes']
        cantidad = request.POST['cantidad']
        pesticidas = request.POST['pesticidas']
        frecuencia = request.POST['frecuencia']
        control_plagas = request.POST['control-plagas']
        sombra = request.POST['sombra']
        porcentaje = request.POST['porcentaje']
        plagas = request.POST['plagas']
        enfermedades = request.POST['enfermedades']
        sintomas_visibles = request.POST['sintomas_visibles']
        problemas_crecimiento = request.POST['problemas-crecimiento']

        # Lógica del algoritmo
        evaluacion = evaluar(altitud, area_cultivada, variedad_cafe, edad_cultivo, densidad_plantacion, sistema_cultivo,
                             date_ultima_cosecha, produccion_anual, tipo_riego, fertilizantes, cantidad, pesticidas,
                             frecuencia, control_plagas, sombra, porcentaje, plagas, enfermedades, sintomas_visibles,
                             problemas_crecimiento)

        # Guardar resultados en la base de datos
        usuario = request.user.usuario
        resultado = ResultadoEvaluacion(
            user=usuario,
            altitud=altitud,
            area_cultivada=area_cultivada,
            variedad_cafe=variedad_cafe,
            edad_cultivo=edad_cultivo,
            densidad_plantacion=densidad_plantacion,
            sistema_cultivo=sistema_cultivo,
            date_ultima_cosecha=date_ultima_cosecha,
            produccion_anual=produccion_anual,
            tipo_riego=tipo_riego,
            fertilizantes=fertilizantes,
            cantidad=cantidad,
            pesticidas=pesticidas,
            frecuencia=frecuencia,
            control_plagas=control_plagas,
            sombra=sombra,
            porcentaje=porcentaje,
            plagas=plagas,
            enfermedades=enfermedades,
            sintomas_visibles=sintomas_visibles,
            problemas_crecimiento=problemas_crecimiento,
            rendimiento_esperado=evaluacion['rendimiento_esperado'],
            sugerencias=", ".join(evaluacion['sugerencias']),
            posibles_problemas_futuros=evaluacion['posibles_problemas_futuros']
        )
        resultado.save()

        return redirect('resultados')

    else:
        return HttpResponse("Método no permitido", status=405)

def evaluar(altitud, area_cultivada, variedad_cafe, edad_cultivo, densidad_plantacion, sistema_cultivo, date_ultima_cosecha,
            produccion_anual, tipo_riego, fertilizantes, cantidad, pesticidas, frecuencia, control_plagas, sombra, porcentaje,
            plagas, enfermedades, sintomas_visibles, problemas_crecimiento):
    
    # Implementación de la evaluación
    rendimiento_base = 1000  # Valor base de rendimiento en kg/ha
    coef_variedad = {'Typica': 0.9, 'Bourbon': 1.0, 'Caturra': 1.1, 'Mundo_Novo': 1.05, 'Geisha': 1.2}
    coef_riego = {'Manual': 0.8, 'Goteo': 1.2, 'aspersion': 1.1}
    coef_fertilizante = {'compost': 1.0, 'nitrato-de-amonio': 1.2}
    coef_pesticidas = {'insecticidas-quimicos': 1.1, 'insecticidas-biologicos': 0.9}
    coef_plagas = {'Broca': 0.8, 'Minador-hoja': 0.7}
    coef_enfermedades = {'Roya-cafe': 0.7, 'Antracnosis': 0.8}
    coef_sombra = {'Guamo': 1.1, 'Cedro': 1.0}
    
    rendimiento = rendimiento_base * coef_variedad.get(variedad_cafe, 1) * coef_riego.get(tipo_riego, 1) \
                  * coef_fertilizante.get(fertilizantes, 1) * coef_pesticidas.get(pesticidas, 1) \
                  * coef_sombra.get(sombra, 1)
    
    # Ajustar por plagas y enfermedades
    if plagas != 'ninguna':
        rendimiento *= coef_plagas.get(plagas, 1)
    if enfermedades != 'ninguna':
        rendimiento *= coef_enfermedades.get(enfermedades, 1)
    
    # Ajustar por síntomas visibles y problemas de crecimiento
    if sintomas_visibles != 'ninguna':
        rendimiento *= 0.9
    if problemas_crecimiento != 'ninguna':
        rendimiento *= 0.9

    # Sugerencias de mejora (esto puede expandirse con más lógica)
    sugerencias = []
    if rendimiento < 800:
        sugerencias.append("Considera cambiar el sistema de riego para mejorar la eficiencia.")
    if fertilizantes == 'compost' and rendimiento < 1000:
        sugerencias.append("Podrías mejorar la fertilización usando abonos químicos balanceados.")
    
    # Resultado final
    evaluacion = {
        'rendimiento_esperado': rendimiento,
        'sugerencias': sugerencias,
        'posibles_problemas_futuros': "Monitorea las plagas y enfermedades regularmente para evitar pérdidas."
    }
    
    return evaluacion

@login_required
def suelo (request):
    return render(request, 'suelo.html')

@login_required
def resultados(request):
    usuario = Usuario.objects.get(user=request.user)
    evaluaciones = ResultadoEvaluacion.objects.filter(user=usuario).order_by('-fecha')
    return render(request, 'resultados.html', {'evaluaciones': evaluaciones})