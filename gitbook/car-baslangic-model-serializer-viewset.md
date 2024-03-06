---
description: >-
  Basit bir model yazdık ve ona endpoint tanımladık, final project ile
  deneyebilirsin
---

# 🏎️ Car Başlangıç Model - Serializer - Viewset

## Start Project

[Start Project](car-app/#start-project)

## Final Project

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

{% code title="car/serializers.py" %}
```python
from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id',
            'plate_number',
            'brand',
            'model',
            'year',
            'gear',
            'rent_per_day',
            'availability',
        )
```
{% endcode %}

{% code title="car/urls.py" %}
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet

router = DefaultRouter()
router.register('cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```
{% endcode %}

{% code title="car/admin.py" %}
```python
from .models import Car

admin.site.register(Car)
```
{% endcode %}
