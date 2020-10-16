# Generated by Django 3.1.2 on 2020-10-16 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('Direccion', models.CharField(max_length=100)),
                ('Correo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('apellidoPaterno', models.CharField(max_length=35)),
                ('apellidoMaterno', models.CharField(max_length=35)),
                ('nombres', models.CharField(max_length=35)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('fechaNacimiento', models.DateField()),
                ('Direccion', models.CharField(max_length=100)),
                ('Correo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.paciente')),
            ],
        ),
    ]