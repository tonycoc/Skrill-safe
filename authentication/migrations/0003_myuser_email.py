# Generated by Django 4.2.4 on 2023-08-22 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_myuser_is_active_myuser_is_staff_myuser_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=254, unique=True),
        ),
    ]
