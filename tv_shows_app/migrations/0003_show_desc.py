# Generated by Django 3.1.3 on 2020-12-02 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0002_auto_20201201_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]