# Generated by Django 3.0.6 on 2020-05-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sistemacliente',
            name='RodapeImagem',
            field=models.ImageField(blank=True, null=True, upload_to='rodapeEmail'),
        ),
    ]
