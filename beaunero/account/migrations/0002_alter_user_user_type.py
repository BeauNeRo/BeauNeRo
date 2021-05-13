# Generated by Django 3.2.2 on 2021-05-13 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('customer', 'Customer'), ('admin', 'Admin')], max_length=20),
        ),
    ]