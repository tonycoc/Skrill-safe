# Generated by Django 4.2.4 on 2023-10-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_temp_token_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
