# Generated by Django 3.2.4 on 2022-12-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_student_sudentnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='des',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='sudentNumber',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
