# Generated by Django 4.2.4 on 2023-09-03 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_usuario_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='condicion',
            field=models.CharField(default='default', max_length=20),
        ),
    ]