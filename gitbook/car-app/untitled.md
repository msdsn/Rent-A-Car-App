---
description: Serializerdaki ufak detayları anlatmak için oluşturuldu
---

# Untitled



```python
from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    is_available = serializers.BooleanField()
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
            'is_available'
        )
```
