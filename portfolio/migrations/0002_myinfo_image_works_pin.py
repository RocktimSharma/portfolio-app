# Generated by Django 4.2.3 on 2023-07-07 11:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myinfo',
            name='image',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='works',
            name='pin',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
