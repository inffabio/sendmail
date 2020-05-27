# Generated by Django 3.0.6 on 2020-05-27 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SistemaCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sistema', models.CharField(max_length=100)),
                ('ServidorEmail', models.CharField(max_length=100)),
                ('LoginServidor', models.CharField(max_length=100)),
                ('SenhaServidor', models.CharField(max_length=50)),
                ('Porta', models.IntegerField()),
                ('SSL', models.BooleanField(default=False)),
            ],
        ),
    ]