# Generated by Django 3.0.9 on 2020-08-04 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0009_add_subregion'),
        ('meetup', '0002_auto_20200804_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='meetup_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.City', verbose_name='Meetup Location'),
        ),
    ]
