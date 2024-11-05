from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from terrenos.models import Terreno
from usuarios.models import Caficultor, Usuario
from .models import ResultadoEvaluacion, ResultadoSuelo
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
def suelo(request):
    try:
        caficultor = request.user.usuario.caficultor
        terrenos = Terreno.objects.filter(caficultor=caficultor)
    except Caficultor.DoesNotExist:
        return HttpResponse("No se encontró un caficultor asociado para este usuario.")
    
    if request.method == 'POST':
        # Función auxiliar para intentar convertir valores de str a float
        def to_float(value, default=0.0):
            try:
                return float(value)
            except (ValueError, TypeError):
                return default
        
        # Captura y convierte los datos de entrada del formulario de análisis de suelo
        altitud = to_float(request.POST.get('altitud'))
        color = request.POST.get('color_suelo', 'medio')
        textura = request.POST.get('textura_suelo', 'arenosa')
        humedad = to_float(request.POST.get('humedad'))
        drenaje = request.POST.get('drenaje-suelo', 'moderado')
        compactacion = request.POST.get('compactacion-suelo', 'media')
        temperatura = to_float(request.POST.get('temperatura'))
        ph = to_float(request.POST.get('ph'))
        nitrogeno = to_float(request.POST.get('nitrogeno'))
        fosforo = to_float(request.POST.get('fosforo'))
        potasio = to_float(request.POST.get('potasio'))
        calcio = to_float(request.POST.get('calcio'))
        magnesio = to_float(request.POST.get('magnesio'))
        azufre = to_float(request.POST.get('azufre'))
        hierro = to_float(request.POST.get('hierro'))
        manganeso = to_float(request.POST.get('manganeso'))
        zinc = to_float(request.POST.get('zinc'))
        cobre = to_float(request.POST.get('cobre'))
        boro = to_float(request.POST.get('boro'))
        molibdeno = to_float(request.POST.get('molibdeno'))
        materia_organica = to_float(request.POST.get('materia_organica'))
        salinidad = to_float(request.POST.get('salinidad'))
        fertilizantes = request.POST.get('fertilizantes', 'moderado')
        cantidades_aplicadas = to_float(request.POST.get('cantidades-aplicadas'))
        frecuencia_aplicacion = to_float(request.POST.get('frecuencia-aplicacion'))
        
        # Aplicar el algoritmo de evaluación con los valores obtenidos
        evaluacion = evaluar_calidad_suelo(
            altitud, color, textura, humedad, drenaje, compactacion, temperatura, ph,
            nitrogeno, fosforo, potasio, calcio, magnesio, azufre, hierro, manganeso,
            zinc, cobre, boro, molibdeno, materia_organica, salinidad, fertilizantes,
            cantidades_aplicadas, frecuencia_aplicacion
        )

        # Guardar los resultados en la base de datos
        usuario = request.user.usuario
        resultado_suelo = ResultadoSuelo(
            user=usuario,
            altitud=altitud,
            color=color,
            textura=textura,
            humedad=humedad,
            drenaje=drenaje,
            compactacion=compactacion,
            temperatura=temperatura,
            ph=ph,
            nitrogeno=nitrogeno,
            fosforo=fosforo,
            potasio=potasio,
            calcio=calcio,
            magnesio=magnesio,
            azufre=azufre,
            hierro=hierro,
            manganeso=manganeso,
            zinc=zinc,
            cobre=cobre,
            boro=boro,
            molibdeno=molibdeno,
            materia_organica=materia_organica,
            salinidad=salinidad,
            fertilizantes=fertilizantes,
            cantidades_aplicadas=cantidades_aplicadas,
            frecuencia_aplicacion=frecuencia_aplicacion,
            calidad_suelo=evaluacion['calidad'],
            recomendaciones=evaluacion['recomendaciones'],
            posibles_riesgos=evaluacion['riesgos']
        )
        resultado_suelo.save()

        return redirect('resultados')
    else:
        return render(request, 'suelo.html', {'terrenos': terrenos})

def evaluar_calidad_suelo(
    altitud, color, textura, humedad, drenaje, compactacion, temperatura, ph,
    nitrogeno, fosforo, potasio, calcio, magnesio, azufre, hierro, manganeso,
    zinc, cobre, boro, molibdeno, materia_organica, salinidad, fertilizantes,
    cantidades_aplicadas, frecuencia_aplicacion
):
    # Valores base y coeficientes para atributos del suelo
    calidad_base = 100
    coef_textura = {'arenosa': 0.8, 'limosa': 1.0, 'arcillosa': 1.1}
    coef_drenaje = {'bueno': 1.0, 'moderado': 0.9, 'deficiente': 0.7}
    coef_compactacion = {'baja': 1.0, 'media': 0.9, 'alta': 0.8}
    coef_color = {'oscuro': 1.1, 'medio': 1.0, 'claro': 0.9}
    coef_humedad = {'baja': 0.8, 'media': 1.0, 'alta': 0.9}

    # Clasificación de humedad
    humedad_categoria = 'baja' if humedad < 30 else 'media' if humedad < 70 else 'alta'
    
    # Cálculo inicial de la calidad del suelo basado en factores físicos
    calidad_suelo = (
        calidad_base
        * coef_textura.get(textura, 1)
        * coef_drenaje.get(drenaje, 1)
        * coef_compactacion.get(compactacion, 1)
        * coef_color.get(color, 1)
        * coef_humedad.get(humedad_categoria, 1)
    )

    # Ajustes por pH, materia orgánica y altitud
    if ph < 5.5 or ph > 7.5:
        calidad_suelo *= 0.9
    if materia_organica < 2.0:
        calidad_suelo *= 0.85
    if altitud > 2000:
        calidad_suelo *= 0.95

    # Evaluación de nutrientes, penalización por deficiencias
    nutrientes = [nitrogeno, fosforo, potasio, calcio, magnesio, azufre, hierro, manganeso, zinc, cobre, boro, molibdeno]
    calidad_suelo *= 0.95 ** sum(1 for n in nutrientes if n < 1.0)

    # Ajustes adicionales por salinidad y fertilizantes
    if salinidad > 1.5:
        calidad_suelo *= 0.85
    if fertilizantes.lower() in ['bajo', 'muy bajo']:
        calidad_suelo *= 0.9

    # Ajuste por cantidades y frecuencia de aplicación de fertilizantes
    if cantidades_aplicadas < 50 or frecuencia_aplicacion < 1:
        calidad_suelo *= 0.95

    # Ajustes según la temperatura
    if temperatura < 15 or temperatura > 25:
        calidad_suelo *= 0.9

    # Recomendaciones
    recomendaciones = []
    if calidad_suelo < 80:
        recomendaciones.append("Mejora la estructura del suelo añadiendo materia orgánica.")
    # (otras recomendaciones…)

    evaluacion = {
        'calidad': calidad_suelo,
        'recomendaciones': recomendaciones,
        'riesgos': "Monitorea la compactación y la erosión para evitar problemas de cultivo."
    }
    return evaluacion


@login_required
def resultados(request):
    usuario = Usuario.objects.get(user=request.user)
    evaluaciones = ResultadoEvaluacion.objects.filter(user=usuario).order_by('-fecha')
    analisis_suelo = ResultadoSuelo.objects.filter(user=usuario).order_by('-fecha')
    return render(request, 'resultados.html', {
        'evaluaciones': evaluaciones,
        'analisis_suelo': analisis_suelo
    })