# Generated by Django 4.2.4 on 2023-09-12 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AirDc', '0002_alter_producto_img_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img_producto',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]