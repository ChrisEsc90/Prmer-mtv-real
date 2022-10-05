from django.http import HttpResponse
from datetime import datetime
from django.template import context, Template, loader
import random

def hola(request):
    return HttpResponse('Hola bebe!')

def fecha(request):
    fecha__y__hora = datetime.now()
    return HttpResponse(f'La fecha y hora actual es{fecha__y__hora}')

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años seria: {fecha}')

def mi_template(request):
    
    cargar_archivo = open(r'C:\Users\ChrisEsc90\Desktop\Proyecto-Clases\templates\template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = context()
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)


def tu_template(request, nombre):
    
    template = loader.get_template('tu_template.html')
    template_renderizado = template.render({'persona': nombre})
    
    return HttpResponse(template_renderizado)

def prueba_template(request):
    mi_contexto = {
        'rango': list(range(1,11)),
        'valor_aleatorio': random.randrange(1,11)
    }
          
    template = loader.get_template('prueba_template.html')
    template_renderizado = template.render(mi_contexto)
    
    return HttpResponse(template_renderizado)