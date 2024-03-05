---
description: Yeni kullanıcı oluşturulmak istendiğinde çalışacak serializer
---

# 🕵️ Register Serializer

{% code title="serializers.py" %}
```python
from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
```
{% endcode %}

djangonun validate password özelliğini kullandım

<pre class="language-python"><code class="lang-python">from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators = [validate_password]
    )
<strong>    # ... [Diğer adımlar]
</strong></code></pre>

Serializer'ın _<mark style="color:orange;">validate</mark>_ metodu sayesinde iki şifrenin eşleşme kontrolünü yaptım

<pre class="language-python"><code class="lang-python"># ... [imports]
class RegisterSerializer(serializers.ModelSerializer):
<strong>    # ... [Öceki adımlar]
</strong>    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
</code></pre>

Serializer'in _<mark style="color:orange;">create</mark>_ sayesinde User modelinden bir satır oluşturup kayıt ettim.

<pre class="language-python"><code class="lang-python"># ... [Önceki importlar]
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
<strong>    # ... [Öceki adımlar]
</strong>    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(password)
        user.save()
        return user
</code></pre>

Yukarıdaki kodda <mark style="color:green;">password2</mark> siliniyor çünkü _<mark style="color:orange;">create</mark>_ metodu çalışmadan önce _<mark style="color:orange;">validate</mark>_ metodu çalışıyor ve <mark style="color:green;">password2</mark> ile <mark style="color:green;">password</mark> aynı mı kontrolu yapılıyor. Dolayısıyla <mark style="color:green;">password2</mark> artık gereksiz.

User object oluşturulurken password eleman olarak verlimiyor çünkü password ile hash oluşturup onu öyle kayıt etmeliyiz ve `user.set_password(password)` diyerek hash ile kayıt edilmiş oluyor, tabi birde save dememiz lazım.
