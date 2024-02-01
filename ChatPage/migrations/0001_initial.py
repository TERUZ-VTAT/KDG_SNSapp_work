# Generated by Django 4.2.3 on 2023-12-30 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sendUser', models.CharField(max_length=128)),
                ('sendMessage', models.TextField()),
                ('sendRoom', models.CharField(max_length=256)),
            ],
        ),
    ]
