# Generated by Django 3.1.5 on 2021-01-25 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
