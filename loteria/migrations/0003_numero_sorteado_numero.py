# Generated by Django 4.0.6 on 2022-10-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loteria', '0002_alter_aposta_jogo'),
    ]

    operations = [
        migrations.AddField(
            model_name='numero_sorteado',
            name='numero',
            field=models.JSONField(default=0),
        ),
    ]
