# Generated by Django 2.2.16 on 2020-09-24 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estagiario', '0006_auto_20200924_0944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estagiario',
            old_name='dt_fim_contrato',
            new_name='fim_contrato',
        ),
        migrations.RenameField(
            model_name='estagiario',
            old_name='dt_inicio_contrato',
            new_name='inicio_contrato',
        ),
    ]
