# Generated by Django 5.0.3 on 2024-03-21 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_recruiter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recruiter',
            old_name='resume',
            new_name='image',
        ),
    ]