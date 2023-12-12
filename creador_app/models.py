from django.db import models
from django.db.models import Model

# Create your models here.
class Creador(Model):
    """
    Atributos de clase que son usadas por herencia de la clase Model

    """
    nombre  =  models.CharField(max_length=400, null = False)
    autor  =  models.CharField(max_length=40, default="Anonimo")
    descripcion  =  models.CharField(max_length=1000)
    creacion = models.DateField(max_length=150,auto_now=True)
    rating  = models.PositiveSmallIntegerField(blank=False,null=False)
    abv     = models.FloatField(blank=True, null=True)

    # podemos crear la tabla con un nombre especifico pero se lo tenemos
    # que indicar directamente en la metaclase

    class Meta:
        db_table = "creador_meta"


    def __str__(self):
        return f"El Creador: {self.nombre}, Rating {self.abv}"

    def get_fields(self):
        """
         Obtiene los nombres y valores de los campos de un modelo.

        Retorna una lista de tuplas donde cada tupla contiene el nombre descriptivo del campo
        y el valor correspondiente para el objeto actual.

        :return: Lista de tuplas (nombre del campo, valor del campo)
        :rtype: list
        """
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]