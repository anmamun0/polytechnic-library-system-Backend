# Generated by Django 5.0.7 on 2025-03-09 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nationality_type',
            field=models.CharField(choices=[('birth', 'birth'), ('nid', 'nid')], max_length=10),
        ),
    ]
