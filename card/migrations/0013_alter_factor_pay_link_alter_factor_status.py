# Generated by Django 4.2.4 on 2023-10-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0012_alter_factor_payed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factor',
            name='pay_link',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='factor',
            name='status',
            field=models.CharField(default='not paid', max_length=500),
        ),
    ]
