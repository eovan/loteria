# Generated by Django 4.0.6 on 2022-10-28 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loteria', '0003_numero_sorteado_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numero_sorteado',
            name='numero',
            field=models.JSONField(default={'numero': []}),
        ),
    ]
