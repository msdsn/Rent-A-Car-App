---
description: >-
  Bu uygulama bir rent a car uygulaması ve çeşitli arabalar yüklenip daha sonra
  bu arabalara reservasyon yapılabilecek.
---

# 🚗 Rent-A-Car-App

> " Rent-A-Car Django backend uygulaması çok anlaşılırdı ve authentication'ın best practice olduğunu söyleyebilirim. Basit ve anlaşılır anlatım sayesinde, hiç zorlanmadan istediğiniz yerden git clone ve git branch yaparak başlayabilirsiniz. Herkese tavsiye ederim.

## Kullanılan araçlar:

* &#x20;<mark style="background-color:green;">django-rest-framework</mark>&#x20;
* &#x20;<mark style="background-color:green;">dj-rest-auth</mark>&#x20;

## Görevler:

### - Customers

<table data-view="cards"><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td><p> <mark style="background-color:green;">Zorluk: Kolay</mark> </p><p>Araç kiralayabilir</p></td><td><ul><li>Kaç gün kiralayacağını söyleyebilir</li></ul></td><td></td></tr><tr><td><p> <mark style="background-color:red;">Zorluk: Zor</mark> </p><p>Uygun araçları görebilir</p></td><td><ul><li>Zaman aralığındaki musait olan araçları göster</li></ul></td><td></td></tr><tr><td><p> <mark style="background-color:yellow;">Zorluk: Normal</mark> </p><p>Aynı anda iki araç kiralayamaz</p></td><td><ul><li>O zaman aralığında başka araç kiralamış mı?</li></ul></td><td></td></tr><tr><td> <mark style="background-color:yellow;">Zorluk: Normal</mark>  </td><td>Reservasyonu güncelleyebilir</td><td><ul><li>Aracın reservasyonunu uzatabilir</li></ul></td></tr><tr><td> <mark style="background-color:red;">Zorluk: Zor</mark> </td><td>İki reservasyon çakışıyorsa güncelleyemez</td><td><ul><li>Eğer bitiş zamanı uzatırken başka araç reservasyonu var ise uzatamaz</li></ul></td></tr><tr><td> <mark style="background-color:green;">Zorluk: Kolay</mark> </td><td>Reservasyonu iptal edebilir</td><td></td></tr></tbody></table>

### - Adminler



<table data-view="cards"><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td> <mark style="background-color:yellow;">Zorluk: Normal</mark> </td><td><em><mark style="color:red;">Car</mark></em> tablosunda CRUD işlemleri yapabilir</td><td><ul><li>Sadece admine özel izinler yazılmalı</li></ul></td></tr><tr><td> <mark style="background-color:yellow;">Zorluk: Normal</mark> </td><td><em><mark style="color:orange;">Customer</mark></em> tablosunda CRUD yapabilir.</td><td></td></tr><tr><td> <mark style="background-color:yellow;">Zorluk: Normal</mark> </td><td><em><mark style="color:red;">Reservasyon</mark></em> tablosunda CRUD yapabilir.</td><td></td></tr></tbody></table>



***

Başlangıç için şuraya bakabilirsin. -> [Başlangıç](baslangic.md)

Authentication için adımlar -> [Authentication](authentication/)

Car uygulaması -> [Car App](car-app/)
