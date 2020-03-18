from django.db import models
from django.conf import settings


class Region(models.Model):
    name = models.CharField("nombre", max_length=50, unique=True)

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"

    def __str__(self):
        return self.name

class Hospital(models.Model):
    city = models.CharField("localidad", max_length=100, blank=True, null=True)
    phone = models.CharField("teléfono", max_length=15)
    name = models.CharField("nombre", max_length=100)
    address = models.CharField("dirección", max_length=255)
    region = models.ForeignKey('Region', verbose_name="región", on_delete=models.CASCADE)
    comment = models.TextField("comentario", blank=True, null=True)

    class Meta:
        verbose_name = "Hospital"
        verbose_name_plural = "Hospitales"

    def __str__(self):
        return f"{self.name} ({self.region})"

class Resource(models.Model):
    name = models.CharField("nombre", max_length=255, unique=True)

    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"

    def __str__(self):
        return self.name

class Need(models.Model):
    hospital = models.ForeignKey('Hospital', verbose_name="hospital", on_delete=models.CASCADE)
    resource = models.ForeignKey('Resource', verbose_name="recurso", on_delete=models.CASCADE)
    amount_per_day = models.PositiveIntegerField('cantidad por día', default=0)
    comment = models.TextField("comentario", blank=True, null=True)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="editor", on_delete=models.CASCADE)
    created_at = models.DateTimeField("alta", auto_now_add=True)
    updated_at = models.DateTimeField("actualizado", auto_now=True)

    class Meta:
        verbose_name = "Necesidad"
        verbose_name_plural = "Necesidades"

    def __str__(self):
        return str(self.resource)