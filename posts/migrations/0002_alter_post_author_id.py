# Generated by Django 4.1.7 on 2024-04-23 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_id',
            field=models.CharField(max_length=128),
        ),
    ]
