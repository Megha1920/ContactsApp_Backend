# Generated by Django 5.0.7 on 2024-07-18 17:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone_number',
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_numbers', to='contacts.contact')),
            ],
        ),
    ]
