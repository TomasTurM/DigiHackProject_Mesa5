from django.db import models

# Create your models here.

class Comprador(models.Model):

    nombre = models.CharField(max_length=20, verbose_name='Nombre')

    apellido = models.CharField(max_length=20, verbose_name='Apellido')

    fecha_nac = models.DateField(auto_now=False, null=True, verbose_name='Fecha')

    dni = models.IntegerField(null=True)

    ciudad = models.CharField(max_length=20)

    direccion = models.CharField(max_length=30)

    email = models.CharField(max_length=50)

    telefono = models.CharField(max_length=15)


    class Meta:
        verbose_name = 'Comprador'


class Vendedor(models.Model):

    nombre = models.CharField(max_length=20, verbose_name='Nombre')

    apellido = models.CharField(max_length=20, verbose_name='Apellido')

    fecha_nac = models.DateField(auto_now=False, null=True, verbose_name='Fecha')

    dni = models.IntegerField(null=True)

    ciudad = models.CharField(max_length=20)

    direccion = models.CharField(max_length=30)

    email = models.CharField(max_length=50)

    telefono = models.CharField(max_length=15)

    zona_com = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Vendedor'


class Producto(models.Model):

    nombre = models.CharField(max_length=20)

    TIPOS = {
        ('Verdura', 'VERDURA'),
        ('Fruta', 'FRUTA'),
    }

    tipo = models.CharField(max_length=15, choices=TIPOS)

    precio = models.DecimalField(max_digits=5, decimal_places=2)