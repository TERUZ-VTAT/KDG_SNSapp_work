# Generated by Django 5.0.1 on 2024-01-31 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResetMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=120)),
                ('new_mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
