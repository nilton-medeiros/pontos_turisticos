# Generated by Django 3.1.4 on 2021-01-05 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endereco',
            old_name='linha1',
            new_name='logradouro',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='linha2',
            new_name='complemento',
        ),
    ]
