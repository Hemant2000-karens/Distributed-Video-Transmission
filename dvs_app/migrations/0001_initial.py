# Generated by Django 5.0.4 on 2024-04-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInteractionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('client_ip', models.CharField(max_length=100)),
                ('action', models.CharField(max_length=100)),
            ],
        ),
    ]
