# Generated by Django 5.0.7 on 2024-07-22 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_user_phone_number_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_numbers',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='PhoneNumber',
        ),
    ]