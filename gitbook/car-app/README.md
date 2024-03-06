# 🚛 Car App

## Start Project

projeye tam bu noktadan başlamak için ->

`git clone git@github.com:msdsn/Rent-A-Car-App.git`

`git branch a8283d7ae0d20555b5a7bbf1ffefaaa22f842baf`

Kurulumu tamamlamak için -> [Başlat](../projeye-istedigin-yerden-basla.md)

## Final Project

Son halini almak için ->

`git clone git@github.com:msdsn/Rent-A-Car-App.git`

`git branch a8283d7ae0d20555b5a7bbf1ffefaaa22f842baf`

Clone kurulumu tamamlamak için -> [Tamamla](../projeye-istedigin-yerden-basla.md)

#### 1. Car Modeli Oluşturdum

{% code title="car/models.py" %}
```python
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
```
{% endcode %}
