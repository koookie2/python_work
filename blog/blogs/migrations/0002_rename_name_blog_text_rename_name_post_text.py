# Generated by Django 4.1.9 on 2023-06-06 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='text',
        ),
    ]
