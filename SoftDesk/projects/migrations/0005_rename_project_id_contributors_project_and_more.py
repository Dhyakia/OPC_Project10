# Generated by Django 4.0.4 on 2022-05-23 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_contributors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributors',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='contributors',
            old_name='user_id',
            new_name='user',
        ),
    ]
