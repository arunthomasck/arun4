# Generated by Django 4.2.2 on 2023-06-20 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_rename_desc_team_details_rename_name_team_employee_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='Image',
            new_name='Img',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='Details',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='Employee',
            new_name='name',
        ),
    ]