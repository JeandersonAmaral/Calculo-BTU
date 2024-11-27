# Generated by Django 4.2.16 on 2024-11-26 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculos_ar_condicionado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=100)),
                ('espessura', models.FloatField()),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camadas', to='calculos_ar_condicionado.ambiente')),
            ],
        ),
    ]