# Generated by Django 5.1.1 on 2024-09-30 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expensiveapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_register',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
