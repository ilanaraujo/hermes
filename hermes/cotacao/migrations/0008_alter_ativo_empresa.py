# Generated by Django 4.1 on 2022-08-08 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao', '0007_alter_ativo_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ativo',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotacao.empresa'),
        ),
    ]
