# Generated by Django 2.2.4 on 2019-08-11 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0004_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=65),
        ),
    ]
