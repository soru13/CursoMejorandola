from django.http import HttpResponse
from django.template.loader import get_template 
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response

def home(request):
    return HttpResponse("Bienvenido")
    
def post(request,id):
    return HttpResponse("Aqui va el post %i" % int(id))
    
def hora(request):
    ahora = datetime.now()
    arreglo = range(20)
    return render_to_response('hora.html', 
                                {'hora': ahora,'arreglo':arreglo})
