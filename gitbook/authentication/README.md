---
description: >-
  dj-rest-auth ve custom Register endpoint kullanılarak hazırlanan user girişini
  ayarlayan app
---

# 🚪 Authentication

## Start project:

`git clone git@github.com:msdsn/Rent-A-Car-App.git`

`git checkout 45e310191bcefe6e8c683b66bf021e2c7e48b62b`

## Final project:

`git clone git@github.com:msdsn/Rent-A-Car-App.git`

`git checkout 7434ea79cbc9365250ba796498f7353a1c6f1a17`

## Adım adım yaptıklarım:

* pip install dj-rest-auth
* python manage.py startapp users

<mark style="background-color:purple;">urls.py</mark> dosyasını users içinde oluşturdum. &#x20;

<mark style="background-color:purple;">serializers.py</mark> isminde bir dosya oluşturdum. [Bir serializer yazdım.](register-serializer.md)

<mark style="background-color:purple;">views.py</mark> dosyasına view ekleyelim. [RegisterView](register-view.md)

<mark style="background-color:red;">users</mark> uygulamasının <mark style="background-color:purple;">urls.py</mark> dosyasını ayarlayalım

{% code title="users/urls.py" %}
```python
from django.urls import path, include
from .views import RegisterView
urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
```
{% endcode %}

Token oluşturmak için signals yazdım. [Signals](signals.md)

Oluşturduğumuz signalin geçerli olması için aşağıdaki gibi <mark style="background-color:purple;">apps.py</mark> dosyasını güncellemeliyiz.

{% code title="apps.py" %}
```python
from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self) -> None:
        import users.signals

```
{% endcode %}

<mark style="background-color:red;">main</mark> içerisindeki <mark style="background-color:purple;">urls.py</mark> ayarını yaptım

{% code title="main/urls.py" %}
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]
```
{% endcode %}

<mark style="background-color:purple;">setting.py</mark> dosyasını ayarladım

```python
INSTALLED_APPS = [
    # ... [Genel Appler]

    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',
    'dj-rest-auth',

    # Local apps
    'users',
]
# ... [Ayarlar]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'users.serializers.CustomTokenSerializer',
}

```

Kendimiz bir token serializer yazıp bunu yukarıdaki gibi ayarlara koyabiliyoruz. Şimdik [CustomTokenSerializer](customtokenserializer.md) yazalım.
