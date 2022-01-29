from django import forms
import django_filters
from django.db.models.base import Model
from .models import LineaInvestigacion, Integrante, Archivo, Producto, Categoria
from django.db.models import Q

# class Filtro(django_filters.FilterSet):
#     class Meta:
#         model = Archivo
#         fields = {
#             'palabras_clave':['icontains'],
#             'nombre_archivo':['icontains']
#         }


class Filtro(django_filters.FilterSet):
    q = django_filters.CharFilter(method='my_custom_filter',label="",widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder':'Buscar'}))

    class Meta:
        model = Archivo
        fields = ['q']
        # widgets = {
        #             'q': forms.Textarea(attrs={'class': 'form-control'}),
        #         }

    def my_custom_filter(self, queryset, name, value):
        return Archivo.objects.filter(
            Q(palabras_clave__icontains=value) | Q(nombre_archivo__icontains=value) | Q(categoria_archivo=value) | Q(lineainvestigacion__nombre_linea__icontains=value)
        ).distinct()


class Palabras_clave(django_filters.FilterSet):
    p = django_filters.CharFilter(method='my_custom_filter',label="Buscar")

    class Meta:
        model = Archivo
        fields = ['p']
        # widgets = {
        #             'p': forms.TextInput(attrs={'class': 'form-control'}),
        #         }

    def my_custom_filter(self, queryset, name, value):
        return Archivo.objects.filter(
            Q(palabras_clave__icontains=value)
        ).distinct()

#
class FiltProductos(django_filters.FilterSet):
    q = django_filters.CharFilter(method='my_custom_filter',label="",widget=forms.TextInput(attrs={'class': 'form-control input-sm', 'placeholder':'Buscar'}))
    palabras_clave = Producto.objects.filter(archivo__palabras_clave='')
    class Meta:
        model = Producto
        fields = ['q']
        # widgets = {
        #             'q': forms.Textarea(attrs={'class': 'form-control'}),
        #         }

    def my_custom_filter(self, queryset, name, value):
        return Producto.objects.filter(
            Q(palabras_clave__icontains=value) | Q(nombre_producto__icontains=value) | Q(categoria_archivo=value) | Q(lineainvestigacion__nombre_linea__icontains=value)
        ).distinct()
