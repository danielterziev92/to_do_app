# Generated by Django 4.0.6 on 2022-07-24 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='priority',
            options={'verbose_name_plural': 'Priority'},
        ),
        migrations.AlterModelOptions(
            name='projectcolor',
            options={'verbose_name_plural': 'Project color'},
        ),
    ]
