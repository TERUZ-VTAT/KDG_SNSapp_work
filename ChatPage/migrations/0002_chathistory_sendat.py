# Generated by Django 4.2.3 on 2024-01-02 03:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ChatPage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chathistory',
            name='sendAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]