# Generated by Django 2.2.16 on 2020-09-23 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estagiario', '0003_auto_20200923_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='estagiario',
            name='telefone_estagiario',
            field=models.CharField(blank=True, max_length=100, verbose_name='Telefone'),
        ),
    ]
