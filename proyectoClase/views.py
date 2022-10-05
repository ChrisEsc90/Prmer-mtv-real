from django.http import HttpResponse
from datetime import datetime

def hola(request):
    return HttpResponse('Hola bebe!')

def fecha(request):
    fecha__y__hora = datetime.now()
    return HttpResponse(f'La fecha y hora actual es{fecha__y__hora}')

