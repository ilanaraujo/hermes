# Generated by Django 4.1 on 2022-08-07 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ativo',
            unique_together={('codigo',)},
        ),
        migrations.AlterUniqueTogether(
            name='empresa',
            unique_together={('codigo',)},
        ),
    ]