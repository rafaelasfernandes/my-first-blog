# Generated by Django 2.2.9 on 2020-01-24 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='data_criacao',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='data_publicacao',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='texto',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titulo',
        ),
    ]
