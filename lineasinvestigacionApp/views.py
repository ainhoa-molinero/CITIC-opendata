from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import LineaInvestigacion, Integrante, Archivo, Producto, Categoria
from .models import LineaInvestigacionTable, ArchivosTable, ProductoTable
from .filters import Filtro
from django_tables2 import RequestConfig


def lineas(request, id_linea):
    obj = LineaInvestigacion.objects.get(pk=id_linea)
    table_linea= LineaInvestigacionTable(LineaInvestigacion.objects.all())
    RequestConfig(request).configure(table_linea)
    table_linea.paginate(page=request.GET.get("page", 1), per_page=50)

    archivos = Archivo.objects.filter(lineainvestigacion__pk=id_linea)
    table_archivos = ArchivosTable(Archivo.objects.filter(lineainvestigacion__pk=id_linea))
    RequestConfig(request).configure(table_archivos)
    table_archivos.paginate(page=request.GET.get("page", 1), per_page=50)

    table_producto = ProductoTable(Producto.objects.filter(lineainvestigacion__pk=id_linea))
    RequestConfig(request).configure(table_producto)
    table_producto.paginate(page=request.GET.get("page", 1), per_page=50)

    return render(request, 'lineasinvestigacionApp/perfil_linea.html', {'obj':obj,'archivos':archivos, 'table_linea':table_linea, 'table_archivos':table_archivos, 'table_producto':table_producto})




def perfil_archivo(request, id_archivo):

    perfil_archivo = Archivo.objects.get(pk=id_archivo)
    return render(request, 'lineasinvestigacionApp/perfil_archivo.html', {'perfil_archivo':perfil_archivo})


def perfil_producto(request, id_producto):

    perfil_producto = Producto.objects.get(pk=id_producto)
    return render(request, 'lineasinvestigacionApp/perfil_producto.html', {'perfil_producto':perfil_producto})


def lista_archivos(request):
    # lista_archivos = Archivo.objects.all()
    filtro = Filtro(request.GET, queryset = Archivo.objects.all())
    # category = Archivo.objects.all().values('categorias').distinct()
    # categories = Archivo.objects.all().values_list('categoria_archivo', flat=True).distinct()
    categories = Categoria.objects.values_list('nombre', flat=True).distinct().order_by('nombre')
    categories = list(categories)
    categories = [ {c : c.replace(' ',  '+')} for c in categories ]

    lines = LineaInvestigacion.objects.values_list('nombre_linea', flat=True).distinct()
    lines = list(lines)
    lines = [ {c : c.replace(' ',  '+')} for c in lines ]

    return render(request, 'lineasinvestigacionApp/lista_archivos.html', {'filtro':filtro, 'categories':categories,  'lines': lines})


def lista_lineas(request):
    # lista_archivos = Archivo.objects.all()
    linea =  LineaInvestigacion.objects.all().order_by('nombre_linea')
    filtro_linea = Filtro(request.GET, queryset = linea)

    return render(request, 'lineasinvestigacionApp/lista_lineas.html', {'filtro_linea':filtro_linea})


def datos_abiertos(request):

    return render(request, 'lineasinvestigacionApp/datosabiertos.html' )


# def categorias(request):
#     categories = Categoria(request.GET, queryset = Archivo.objects.all())
#     return render(request, 'lineasinvestigacionApp/lista_archivos.html', {'categories':categories})
