# Generated by Django 4.1.3 on 2022-12-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity',
            name='description',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]
