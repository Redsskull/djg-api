# Generated by Django 4.2.8 on 2024-02-09 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_imahe_filter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='imahe_filter',
            new_name='image_filter',
        ),
    ]
