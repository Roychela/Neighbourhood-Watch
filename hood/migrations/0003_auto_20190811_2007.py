# Generated by Django 2.2.4 on 2019-08-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_auto_20190811_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='neighbourhood_name',
            field=models.CharField(max_length=100),
        ),
    ]