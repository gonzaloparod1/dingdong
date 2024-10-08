# Generated by Django 5.1 on 2024-09-18 12:40

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('cod', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_name', models.CharField(max_length=64)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('cod', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=1500)),
                ('m2_construidos', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('m2_totales', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('num_estacionamientos', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_habitaciones', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('num_baños', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('direccion', models.CharField(max_length=255)),
                ('tipo_inmueble', models.CharField(choices=[('casa', 'Casa'), ('departamento', 'Departamento'), ('bodega', 'Bodega'), ('parcela', 'Parcela')], max_length=255)),
                ('precio', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1000)])),
                ('precio_ufs', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(1.0)])),
                ('disponible', models.BooleanField(default=True)),
                ('arrendador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='inmuebles', to=settings.AUTH_USER_MODEL)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='inmuebles', to='m7_python.comuna')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='comunas', to='m7_python.region'),
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('rechazada', 'Rechazada'), ('aprobada', 'Aprobada'), ('finalizada', 'Finalizada')], default='pendiente', max_length=50)),
                ('arrendatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes_arrendatario', to=settings.AUTH_USER_MODEL)),
                ('inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='m7_python.inmueble')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=9, unique=True)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(blank=True, max_length=255, null=True)),
                ('rol', models.CharField(choices=[('arrendador', 'Arrendador'), ('arrendatario', 'Arrendatario')], default='arrendatario', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
