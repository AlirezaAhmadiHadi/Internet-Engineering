# Generated by Django 3.2.4 on 2023-01-27 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20230127_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='course',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='student',
            name='owner',
        ),
    ]