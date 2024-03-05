---
description: >-
  dj-rest-auth ve custom Register endpoint kullanılarak hazırlanan user girişini
  ayarlayan app
---

# 🚪 Authentication

## Başlangıç Noktası:

`git clone git@github.com:msdsn/Rent-A-Car-App.git`

`git checkout 45e310191bcefe6e8c683b66bf021e2c7e48b62b`

## Adım adım yaptıklarım:

* pip install dj-rest-auth
* python manage.py startapp users

<mark style="background-color:purple;">urls.py</mark> dosyasını users içinde oluşturdum. &#x20;

<mark style="background-color:purple;">serializers.py</mark> isminde bir dosya oluşturdum. [Bir serializer yazdım.](register-serializer.md)
