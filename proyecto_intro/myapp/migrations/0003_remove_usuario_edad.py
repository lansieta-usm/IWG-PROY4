# Generated by Django 4.2.4 on 2023-09-03 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_usuario_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='edad',
        ),
    ]
