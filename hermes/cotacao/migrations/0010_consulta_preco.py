# Generated by Django 4.1 on 2022-08-08 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao', '0009_consulta_ativomonitorado'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='preco',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
