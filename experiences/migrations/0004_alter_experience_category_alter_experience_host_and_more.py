# Generated by Django 4.1.3 on 2022-12-20 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_alter_category_kind'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiences', '0003_experience_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='category',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experiences', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experience',
            name='perks',
            field=models.ManyToManyField(related_name='experiences', to='experiences.perk'),
        ),
    ]
