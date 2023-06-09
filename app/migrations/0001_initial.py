# Generated by Django 4.1.7 on 2023-03-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Ismi')),
                ('number', models.CharField(max_length=500, verbose_name='Raqami')),
                ('passport', models.ImageField(upload_to='', verbose_name='Passport')),
                ('selfie', models.ImageField(upload_to='', verbose_name='Selfie')),
                ('card', models.CharField(max_length=500, verbose_name='Karta')),
                ('time', models.CharField(max_length=500, verbose_name='Amal qilish muddati')),
                ('model', models.CharField(max_length=500, verbose_name='Model')),
                ('phone', models.CharField(max_length=500, verbose_name='Nomi')),
                ('color', models.CharField(max_length=500, verbose_name='Rangi')),
                ('type', models.CharField(max_length=500, verbose_name='Turi')),
                ('file', models.FileField(max_length=500, upload_to='', verbose_name='Kelishuv')),
                ('status', models.BooleanField(default=False, verbose_name='Holati')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Sana')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200, verbose_name='Model')),
                ('name', models.CharField(max_length=200, verbose_name='Nomi')),
                ('photo', models.ImageField(upload_to='', verbose_name='Rasmi')),
                ('descr', models.TextField(verbose_name='Tavsif')),
                ('color', models.CharField(max_length=200, verbose_name='Rangi')),
                ('month_3', models.CharField(max_length=200, verbose_name='3 oy')),
                ('month_4', models.CharField(max_length=200, verbose_name='4 oy')),
                ('month_6', models.CharField(max_length=200, verbose_name='6 oy')),
                ('month_8', models.CharField(max_length=200, verbose_name='8 oy')),
                ('month_12', models.CharField(max_length=200, verbose_name='12 oy')),
                ('minimum', models.CharField(max_length=200, verbose_name="Boshlangich to'lov")),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Sana')),
            ],
        ),
    ]
