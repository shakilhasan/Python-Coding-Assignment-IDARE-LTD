from django.db import models

# Create your models here.

class Pipe(models.Model):
    pipe_diameter = models.FloatField(default=10.75)
    pipe_thicknes = models.FloatField(default=0.5)
    pipe_density  = models.FloatField(default=490)
    corrosion_allowance = models.FloatField(default=0.125)

    coating_thicknes = models.FloatField(default=0.0118110236220472)
    coating_density = models.FloatField(default=81.156348)

    air_density = models.FloatField(default=0)
    water_density = models.FloatField(default=64)
    sea_density = models.FloatField(default=64.7)

    def __str__(self):
        return str(self.id)
