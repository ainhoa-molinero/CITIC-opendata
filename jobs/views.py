from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from .models import Job
from lineasinvestigacionApp.forms import ArchivoForm
from django.utils import timezone
from lineasinvestigacionApp.models import LineaInvestigacion, Archivo
#
def home(request):
    # jobs = Job.objects
    archivos = Archivo.objects.order_by('-fecha').distinct()
    archivo_dicc = {}
    for a in archivos:
        if a.id_archivo not in archivo_dicc.keys():
            archivo_dicc[a.id_archivo] = a
        archivos = [v for v in archivo_dicc.values() ]
    if request.user.is_authenticated:
        lineas = LineaInvestigacion.objects.order_by('-archivo__fecha').distinct()
        lineas_dicc = {}
        for l in lineas:
            if l.id_linea not in lineas_dicc.keys():
                print(l)
                lineas_dicc[l.id_linea] = l
        lineas = [v for v in lineas_dicc.values() ]
    else:
        # lineas = LineaInvestigacion.objects.filter(visibilidad='publico')
        lineas = LineaInvestigacion.objects.order_by('-archivo__fecha').distinct()
        lineas_dicc = {}
        for l in lineas:
            if l.id_linea not in lineas_dicc.keys():
                print(l)
                lineas_dicc[l.id_linea] = l
        lineas = [v for v in lineas_dicc.values() ]

    return render(request, 'jobs/home.html', {'lineas':lineas[0:2], 'archivos':archivos[0:3]})


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



@login_required
def edit_form(request, id_archivo):
    obj = get_object_or_404(Archivo, pk=id_archivo)
    if request.method == 'POST':
        form = ArchivoForm(request.POST)
        if form.is_valid():
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
        datos = get_object_or_404(Archivo, pk=id_archivo)
        form = ArchivoForm(initial=model_to_dict(datos))

    context = {
        'form':form
    }

    return render(request, 'jobs/editar_dataset.html', {'form':form})





def detail(request, job_id):
    job = get_object_or_404(Archivo, pk=job_id)
    return render(request,  'lineasinvestigacionApp/perfil_archivo.html', {'job':job })
