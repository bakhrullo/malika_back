from django.db import models


class Phone(models.Model):
    model = models.CharField(max_length=200, verbose_name="Model")
    name = models.CharField(max_length=200, verbose_name="Nomi", unique=True)
    photo = models.ImageField(verbose_name="Rasmi", null=True, blank=True, upload_to='photos/items/%Y/%m/%d/',)
    descr = models.TextField(verbose_name="Tavsif")
    color = models.CharField(max_length=200, verbose_name="Rangi")
    month_3 = models.CharField(max_length=200, verbose_name="3 oy")
    month_4 = models.CharField(max_length=200, verbose_name="4 oy")
    month_6 = models.CharField(max_length=200, verbose_name="6 oy" )
    month_8 = models.CharField(max_length=200, verbose_name="8 oy" )
    month_12 = models.CharField(max_length=200, verbose_name="12 oy" )
    minimum = models.CharField(max_length=200, verbose_name="Boshlangich to'lov" )
    date = models.DateTimeField(auto_now_add=True, verbose_name="Sana")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tovarlar"
        verbose_name_plural = "Tovarlar"


class Order(models.Model):
    name = models.CharField(max_length=500, verbose_name="Ismi")
    number = models.CharField(max_length=500, verbose_name="Raqami")
    passport = models.ImageField(verbose_name="Passport", upload_to='photos/orders/%Y/%m/%d/')
    selfie = models.ImageField(verbose_name="Selfie", upload_to='photos/orders/%Y/%m/%d/')
    card = models.CharField(max_length=500, verbose_name="Karta")
    time = models.CharField(max_length=500, verbose_name="Amal qilish muddati")
    model = models.CharField(max_length=500, verbose_name="Model")
    phone = models.CharField(max_length=500, verbose_name="Nomi")
    color = models.CharField(max_length=500, verbose_name="Rangi")
    type = models.CharField(max_length=500, verbose_name="Turi")
    file = models.FileField(max_length=500, verbose_name="Kelishuv", null=True, upload_to='docs/%Y/%m/%d/')
    status = models.BooleanField(default=False, verbose_name="Holati")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Sana")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Buyurtmalar"
        verbose_name_plural = "Buyurtmalar"
