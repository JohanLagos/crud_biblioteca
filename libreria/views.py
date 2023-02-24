from django.shortcuts import get_object_or_404, render
from .models import libro
from .form import LibroForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

#Acceso al sitio:
@login_required
def inicio(request):
    return render(request, 'paginas/inicio.html')

@login_required
def nosotros(request):
    return render(request, 'paginas/nosotros.html')


#Acceso a las paginas:
@login_required
def libros(request):
    libros = libro.objects.all() #traemos todos los datos del objeto
    return render(request, 'libros/index.html', {'Libros' : libros})


# def crear(request):
#     return render(request, 'libros/crear.html')


def editar(request, id):
    libro1 = libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro1)
    if formulario.is_valid and request.POST:
        formulario.save()
    return render(request, 'libros/editar.html', {'formulario':formulario})


def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html' , {'formulario': formulario})


def borrar(request, id):
    libro_borrar = libro.objects.get(id=id)
    libro_borrar.delete()
    return redirect('libros')

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("inicio")
