# Generated by Django 4.1 on 2025-01-11 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_author_testbool'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='testbool',
        ),
    ]
