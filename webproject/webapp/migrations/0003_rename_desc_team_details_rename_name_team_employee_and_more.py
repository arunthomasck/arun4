# Generated by Django 4.2.2 on 2023-06-19 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='desc',
            new_name='Details',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='Employee',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='img',
            new_name='Image',
        ),
    ]
