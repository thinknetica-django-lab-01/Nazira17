# Generated by Django 3.1.5 on 2021-02-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210217_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, default='2021-02-17 19:26:46.675497', verbose_name='add date'),
            preserve_default=False,
        ),
    ]
