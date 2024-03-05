---
description: >-
  Hesap oluşturulmasını sağlayan bir endpoint oluşturma ve hesap oluştuğunda
  token ile birlikte kullanıcıya yanıt dönme
---

# 🎥 Register View

## Start project

Eğer bu sayda yapılanları yapmak istiyorsan ve bundan öncekileri yapmadıysan git clone yapıp direkt bu sayfadan başlayabilirsin.

* `git clone git@github.com:msdsn/Rent-A-Car-App.git`
* `git branch 10ba9621d8b8f363324c2ae063fb7cd94d9c02d4`

## Adım adım işlemler

<mark style="background-color:red;">users</mark> app'i içindeki <mark style="background-color:purple;">views.py</mark> dosyası içine basit bir <mark style="background-color:yellow;">CreateAPIView</mark> yazarak başlıyorum

```python
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
```

post işlemi yapıldığında çalışacak olan _<mark style="color:orange;">create</mark>_ metodunu yazıcam. **Amacımız kullanıcıya token döndürmek**

```python
# ... [Önceki İmportlar]
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

class RegisterView(CreateAPIView):
    # ... [Önceki Adımlar]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user)
        data = serializer.data
        data['token'] = token.key
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
    

```

