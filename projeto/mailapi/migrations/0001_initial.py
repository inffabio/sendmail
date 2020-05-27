# Generated by Django 3.0.6 on 2020-05-27 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emailapi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmailOrigem', models.CharField(max_length=100)),
                ('EmailDestino', models.CharField(max_length=100)),
                ('Assunto', models.CharField(max_length=100, null=True)),
                ('Conteudo', models.TextField()),
                ('Data', models.DateTimeField(auto_now=True)),
                ('Cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.SistemaCliente')),
            ],
        ),
    ]
