from django.shortcuts import render
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def investigaciones(request):
    return render(request, 'paginas/investigaciones.html')
def iniciarSesion(request):
    return render(request, 'paginas/iniciarSesion.html')
def contactenos(request):
    return render(request, 'paginas/contactenos.html')

def familiaCuidador(request):
    return render(request, 'ayuda/familiaCuidador.html')
def pam(request):
    return render(request, 'ayuda/pam.html')
def personalAcreditado(request):
    return render(request, 'ayuda/personalAcreditado.html')

def capacitacionCuidados(request):
    return render(request, 'Servicios/capacitacionCuidados.html')
def edm(request):
    return render(request, 'Servicios/edm.html')
def enc(request):
    return render(request, 'Servicios/enc.html')
def isa(request):
    return render(request, 'Servicios/isa.html')
def reporteClinico(request):
    return render(request, 'Servicios/reporteClinico.html')