from django.db import models
from django.core.validators import MinValueValidator

class Car(models.Model):
    plate_number = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.SmallIntegerField()
    gear = models.CharField(max_length=1, choices=(('A', 'Automatic'), ('M', 'Manual')))
    rent_per_day = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        validators=[MinValueValidator(1.0)]
    )
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.model} - {self.brand} - {self.plate_number}"