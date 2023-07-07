# Generated by Django 4.2.3 on 2023-07-07 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('email', models.CharField(blank=True, max_length=70)),
                ('phone', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=50)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField(blank=True)),
                ('isOngoing', models.BooleanField(blank=True, default=True)),
                ('desc', models.TextField()),
                ('images', models.TextField()),
                ('tools', models.TextField()),
                ('language', models.TextField()),
                ('keyPoints', models.TextField(blank=True, null=True)),
                ('link', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('download', models.URLField(blank=True)),
            ],
        ),
    ]
