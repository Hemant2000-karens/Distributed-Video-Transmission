# Generated by Django 5.0.4 on 2024-04-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvs_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BroadcastingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broadcast_time', models.DateTimeField()),
                ('timezone', models.CharField(max_length=100)),
                ('video_filename', models.CharField(max_length=255)),
            ],
        ),
    ]
