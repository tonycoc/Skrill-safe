# Generated by Django 4.2.4 on 2023-08-25 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_temp_token_created_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='temp_token',
            options={'verbose_name': 'Temp Token', 'verbose_name_plural': 'Temp Tokens'},
        ),
    ]
