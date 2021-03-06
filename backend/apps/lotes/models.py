from django.db import models
from apps.dependencias.models import Dependencia


class Lote(models.Model):
    descripcion = models.CharField(null=False, blank=False, max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True)
    dependencia_destino_id = models.ForeignKey(Dependencia, db_column='dependencia_destino_id', null=False, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Lotes"

    def __str__(self):
        return str(self.id)+" - "+str(self.descripcion)+"/"+str(self.dependencia_destino_id)

