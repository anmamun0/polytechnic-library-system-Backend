# Generated by Django 5.0.7 on 2025-03-22 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
