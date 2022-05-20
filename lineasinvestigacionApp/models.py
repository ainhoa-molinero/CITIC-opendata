from django.db import models
from django.conf import settings
import django_tables2 as tables
import django_filters
from django_tables2.utils import A

class Integrante(models.Model):
    id_integrante = models.AutoField(primary_key=True)
    nombre_integrante = models.CharField(max_length=255)
    cargo = models.CharField(max_length =300)
    def __str__(self):
        return str(self.nombre_integrante)


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=255)
    url_producto = models.URLField(max_length=255, null=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    pub_date =  models.DateTimeField()
    def __str__(self):
        return str(self.nombre_producto)

class Categoria(models.Model):
        nombre = models.CharField(primary_key=True, max_length=255)
        def __str__(self):
            return str(self.nombre)




class Archivo(models.Model):
    id_archivo = models.AutoField(primary_key=True)
    nombre_archivo = models.CharField(max_length=255)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    descripcion_archivo = models.TextField(max_length=500,  null=True, blank=True)
    categoria_archivo = models.ManyToManyField(Categoria, max_length=500, blank=True)
    palabras_clave = models.CharField(max_length=255,  null=True, blank=True)
    url_archivo = models.URLField(max_length=255, null=True, blank=True)
    producto_asociado = models.ManyToManyField(Producto, blank=True)
    fecha =  models.DateTimeField()
    datamod_archivo =  models.DateTimeField( auto_now=True, null=True, blank=True)
    informacion_contacto= models.CharField(max_length=255,  null=True, blank=True)
    formato = models.CharField(max_length=255,  null=True, blank=True)
    licencia = models.CharField(max_length=255,  null=True)
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return str(self.nombre_archivo)
    def listar_palabras_clave(self):
        try:
            return self.palabras_clave.split(',')
        except:
            return None



class LineaInvestigacion(models.Model):
    id_linea = models.AutoField(primary_key=True)
    nombre_linea = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/', null=True, blank=True)
    #icon = models.ImageField(upload_to = 'images/')
    visibilidad = models.CharField(max_length=10, choices=(('publico','publico'),('privado','privado')), default='publico')
    # hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    integrante = models.ManyToManyField(Integrante, blank=True)
    archivo = models.ManyToManyField(Archivo, blank=True)
    producto = models.ManyToManyField(Producto, blank=True)
    imgheader = models.ImageField(upload_to = 'images/', blank = True)
    def __str__(self):
        return str(self.nombre_linea)


class Permiso(models.Model):
    id_linea = models.ForeignKey(LineaInvestigacion, on_delete=models.CASCADE,related_name='id_permiso')
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    permiso = models.CharField(max_length=10, choices=(('Jefe', 'Jefe'), ('Técnico', 'Técnico'), ( 'Admin', 'Admin')))
    def __str__(self):
        return str(self.id_usuario) +' - '+ str(self.id_linea)

class LineaInvestigacionTable(tables.Table):
    class Meta:
        model = LineaInvestigacion
        template_name = "table_template.html"

class ArchivosTable(tables.Table):
    nombre_archivo = tables.LinkColumn("perfil_archivo", args=[A('id_archivo')])
    url_archivo = tables.URLColumn()
    class Meta:
        model = Archivo
        fields = ('nombre_archivo', 'url_archivo', 'pub_date')
        template_name = "table_template.html"

class ProductoTable(tables.Table):
    nombre_producto = tables.LinkColumn("perfil_producto", args=[A('id_producto')])

    class Meta:
        model = Producto
        fields = ('nombre_producto', 'url_producto', 'pub_date')
        template_name = "table_template.html"
