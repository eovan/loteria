# Generated by Django 4.0.6 on 2022-11-03 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loteria', '0009_numero_apostados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numero_apostados',
            name='jogo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loteria.jogos', verbose_name='jogo'),
        ),
    ]
