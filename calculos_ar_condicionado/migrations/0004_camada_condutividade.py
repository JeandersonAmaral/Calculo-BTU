# Generated by Django 4.2.16 on 2024-11-26 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculos_ar_condicionado', '0003_remove_camada_ambiente_ambiente_camadas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='camada',
            name='condutividade',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
    ]
