# Generated by Django 4.0.3 on 2022-05-17 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_profile_ethnicity_alter_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='user',
            new_name='profile',
        ),
        migrations.AlterField(
            model_name='profile',
            name='ethnicity',
            field=models.TextField(default='WHITE', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='kids',
            field=models.TextField(default='NOT SURE YET', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='looking_for',
            field=models.TextField(default='BOTH', max_length=6),
        ),
        migrations.AlterField(
            model_name='profile',
            name='relationship_type',
            field=models.TextField(default='DONT KNOW YET', max_length=100),
        ),
    ]
