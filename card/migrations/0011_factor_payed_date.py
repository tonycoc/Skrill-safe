# Generated by Django 4.2.4 on 2023-09-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0010_alter_card_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='factor',
            name='payed_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
