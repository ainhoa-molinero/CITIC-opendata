from django import forms
from django.db.models.base import Model
from django.forms import ModelForm

from .models import LineaInvestigacion, Archivo

class ArchivoForm(ModelForm):
    categorias = [(i,i) for i in Archivo.objects.values_list('categoria_archivo', flat=True).distinct()]
    nombre_linea = forms.ModelChoiceField(queryset=LineaInvestigacion.objects.all() , required=True)
    fecha = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    categoria_archivo = forms.MultipleChoiceField(choices=categorias, required=True, widget=forms.CheckboxSelectMultiple(attrs={'class':'ul-no-bullets '}))#
    class Meta:
        model = Archivo
        fields = '__all__'
        widgets = {
            'nombre_archivo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_archivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'informacion_contacto' : forms.EmailInput(attrs={'class': 'form-control'}),


            'palabras_clave' : forms.TextInput(attrs={'class': 'form-control'}),
            'url_archivo' : forms.TextInput(attrs={'class': 'form-control'}),
            'producto_asociado' : forms.Select(attrs={'class': 'form-control'}),
            'formato' : forms.TextInput(attrs={'class': 'form-control'}),
            'licencia' : forms.TextInput(attrs={'class': 'form-control'}),
            'fecha' : forms.DateInput(attrs={'type': 'date'}),
        }
        # widgets = {'categoria_archivo': forms.CheckboxSelectMultiple()}
        # fields = ['nombre_archivo', 'descripcion_archivo', 'categoria_archivo', 'palabras_clave', 'url_archivo', 'producto_asociado', 'pub_date', 'datamod_archivo', 'informacion_contacto', 'formato', 'licencia']
