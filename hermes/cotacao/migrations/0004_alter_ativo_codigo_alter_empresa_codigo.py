# Generated by Django 4.1 on 2022-08-07 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao', '0003_alter_ativo_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ativo',
            name='codigo',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='codigo',
            field=models.CharField(max_length=4),
        ),
    ]