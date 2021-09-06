from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job
from lineasinvestigacionApp.forms import ArchivoForm
from django.utils import timezone
from lineasinvestigacionApp.models import LineaInvestigacion, Archivo
#
def home(request):
    # jobs = Job.objects
    if request.user.is_authenticated:
        lineas = LineaInvestigacion.objects.all()
    else:
        lineas = LineaInvestigacion.objects.filter(visibilidad='publico')

    return render(request, 'jobs/home.html', {'lineas':lineas})


# @login_required
# def create(request):
#     if request.method == 'POST':
#         if request.POST['nombre_archivo'] and request.POST['descripcion_archivo'] and request.POST['categoria_archivo'] and request.POST['palabras_clave'] and request.POST['url_archivo']  :
#             archivo = Archivo()
#             archivo.nombre_archivo = request.POST['nombre_archivo']
#             archivo.descripcion_archivo = request.POST['descripcion_archivo']
#
#
#             if request.POST['url_archivo'].startswith('http://') or request.POST['url_archivo'].startswith('https://'):
#                 archivo.url = request.POST['url_archivo']
#             else:
#                 archivo.url = 'http://' + request.POST['url_archivo']
#                 # job.icon = request.FILES['icon']
#                 # job.image = request.FILES['image']
#                 archivo.pub_date = timezone.datetime.now()
#                 # archivo.hunter = request.user
#                 archivo.save()
#                 return redirect('/jobs/' + str(archivo.id_archivo))
#         else:
#             return render(request, 'jobs/create.html', {'error':'Rellena todos los huecos'})
#
#     else:
#         return render(request, 'jobs/create.html')

@login_required
def create(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form = form.cleaned_data
            linea = form.pop('nombre_linea', None)

            obj, _ = Archivo.objects.get_or_create(
                nombre_archivo = form['nombre_archivo'],
                fecha = form['fecha'],
                descripcion_archivo = form['descripcion_archivo'],
                palabras_clave = form['palabras_clave'],
                url_archivo = form['url_archivo'],
                datamod_archivo = form['datamod_archivo'],
                informacion_contacto = form['informacion_contacto'],
                formato = form['formato'],
                licencia = form['licencia'],
            )
            # Subir campos many to many
            obj.categoria_archivo.set(form['categoria_archivo'])
            obj.producto_asociado.set(form['producto_asociado'])

            # Asociar a Lineas


            # Guardar
            obj.save()


            # Asociar archivo a linea investigacion

    else:
        form = ArchivoForm()

    context = {
        'form':form
    }

    return render(request, 'jobs/create.html', {'form':form})





def detail(request, job_id):
    job = get_object_or_404(Archivo, pk=job_id)
    return render(request,  'lineasinvestigacionApp/perfil_archivo.html', {'job':job })
