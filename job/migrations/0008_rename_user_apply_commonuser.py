# Generated by Django 5.0.3 on 2024-03-23 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_apply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='user',
            new_name='commonuser',
        ),
    ]