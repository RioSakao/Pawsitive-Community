# Generated by Django 4.2 on 2024-03-04 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeline',
            old_name='comment',
            new_name='content',
        ),
    ]
