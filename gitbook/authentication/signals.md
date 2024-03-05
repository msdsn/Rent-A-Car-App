---
description: Kullanıcı oluşturulduğunda Token oluşturmayı tetiklemek için
---

# 📶 Signals

## Start project

Eğer bu sayda yapılanları yapmak istiyorsan ve bundan öncekileri yapmadıysan git clone yapıp direkt bu sayfadan başlayabilirsin.

* `git clone git@github.com:msdsn/Rent-A-Car-App.git`
* `git branch c5c59aa0ce3c89a31590123565b9601149dabca4`

## Adım adım işlemler

<mark style="background-color:red;">users</mark> uygulaması içine <mark style="background-color:purple;">signals.py</mark> isminde bir dosya oluşturuyorum

```python
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

_<mark style="color:orange;">post\_save</mark>_ kullanarak bir signal oluşturduk ve yeni <mark style="color:red;">User</mark> oluştuğunda onun için bir token oluşturuyoruz ve <mark style="color:red;">Token</mark> tablosuna kayıt ediyoruz.
