from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Organisatie(models.Model):
    # nummer = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999),MinValueValidator(00000000)])
    nummer = models.IntegerField(
            primary_key=True,
            validators=[
                MinValueValidator(10_000_000), # minimum waarde is dus 10.000.000
                MaxValueValidator(99_999_999), # maximum waarde is dus 99.999.999
            ],
            unique=True
        )
    naam = models.CharField(
            max_length=30,
            unique=True,
        )

    class Meta:
        ordering = ["-naam"]

    def __str__(self):
        return self.naam