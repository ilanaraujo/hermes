# Generated by Django 4.1 on 2022-08-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao', '0002_alter_ativo_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ativo',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='empresa',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='ativo',
            name='codigo',
            field=models.CharField(max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='codigo',
            field=models.CharField(max_length=4, unique=True),
        ),
    ]
