# Generated by Django 4.2.4 on 2023-09-03 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='codigo',
            field=models.TextField(default='default'),
        ),
    ]