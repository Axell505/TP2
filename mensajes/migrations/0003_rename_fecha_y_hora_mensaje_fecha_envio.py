# Generated by Django 4.2 on 2024-09-10 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensajes', '0002_rename_fecha_envio_mensaje_fecha_y_hora_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='fecha_y_hora',
            new_name='fecha_envio',
        ),
    ]
