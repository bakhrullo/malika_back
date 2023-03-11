# Generated by Django 4.1.7 on 2023-03-11 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_phone_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='passport',
            field=models.ImageField(upload_to='photos/orders/%Y/%m/%d/', verbose_name='Passport'),
        ),
        migrations.AlterField(
            model_name='order',
            name='selfie',
            field=models.ImageField(upload_to='photos/orders/%Y/%m/%d/', verbose_name='Selfie'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/items/%Y/%m/%d/', verbose_name='Rasmi'),
        ),
    ]
