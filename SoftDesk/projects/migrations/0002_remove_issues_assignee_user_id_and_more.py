# Generated by Django 4.0.4 on 2022-05-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issues',
            name='assignee_user_id',
        ),
        migrations.RemoveField(
            model_name='issues',
            name='author_user_id',
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='projects',
            name='type',
            field=models.CharField(choices=[('WEB', 'Website'), ('DRO', 'Android'), ('IOS', 'IOS')], max_length=30),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Contributors',
        ),
        migrations.DeleteModel(
            name='Issues',
        ),
    ]