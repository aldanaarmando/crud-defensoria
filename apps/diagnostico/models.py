from django.db import models

# Create your models here.

class diagnostico(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    nombre_diagnostico = models.CharField(max_length = 200, blank = False, null = False)
    descripcion_diagnostico = models.CharField(max_length = 200, blank = False, null = False)

    class Meta:
        verbose_name = 'diagnostico'
        verbose_name_plural = 'diagnosticos'
        ordering = ['nombre_diagnostico']

    def __str__(self):
        return self.nombre_diagnostico

class especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key = True)
    nombre_especialidad = models.CharField(max_length = 200, blank = False, null = False)

    class Meta:
        verbose_name = 'especialidad'
        verbose_name_plural = 'especialidades'
        ordering = ['nombre_especialidad']

    def __str__(self):
        return self.nombre_especialidad
    

class experto(models.Model):
    id_experto = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200)
    apellido = models.CharField(max_length = 200)
    id_especialidad = models.OneToOneField(especialidad, on_delete = models.CASCADE, default = None)

    class Meta:
        verbose_name = 'experto'
        verbose_name_plural = 'expertos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
