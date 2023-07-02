# Generated by Django 4.2.2 on 2023-06-28 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductosMinimos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300, verbose_name='Nombre')),
                ('descripcion', models.CharField(default='Sin descripción', max_length=300, verbose_name='Descripción')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Precio')),
                ('fecha_de_registro', models.DateField(verbose_name='Fecha de registro')),
                ('estatus', models.CharField(max_length=300, verbose_name='Estatus')),
            ],
        ),
    ]
