# Generated by Django 2.2.4 on 2019-08-11 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_auto_20190811_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buiness_name', models.TextField()),
                ('show_email', models.BooleanField(default=True)),
                ('business_description', models.TextField(default='Trading business')),
                ('business_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.Profile')),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='hood.Neighbourhood')),
            ],
        ),
    ]