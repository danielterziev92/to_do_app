# Generated by Django 4.0.6 on 2022-07-24 07:10

import django.core.validators
from django.db import migrations, models
import to_do_app.commons.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modify_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), to_do_app.commons.validators.only_letters_validator])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), to_do_app.commons.validators.only_letters_validator])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('picture', models.ImageField(upload_to='profile')),
                ('day_of_birth', models.DateTimeField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], max_length=11, null=True)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
