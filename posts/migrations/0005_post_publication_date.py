# Generated by Django 4.1.7 on 2024-04-29 17:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_post_author_id_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publication_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
