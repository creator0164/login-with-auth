# Generated by Django 3.2.9 on 2021-12-30 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211230_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='phone_number',
        ),
    ]
