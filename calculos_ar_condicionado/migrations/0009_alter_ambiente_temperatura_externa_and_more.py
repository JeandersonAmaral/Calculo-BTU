# Generated by Django 4.2.16 on 2024-11-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculos_ar_condicionado', '0008_ambiente_temperatura_externa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambiente',
            name='temperatura_externa',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ambiente',
            name='temperatura_interna',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
