# Generated by Django 4.0.1 on 2022-05-16 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_items_carrito'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('Apellido', models.CharField(max_length=200)),
                ('Rut', models.CharField(max_length=200)),
                ('Direccion', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('contrasenia', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'db_usuario',
            },
        ),
    ]
