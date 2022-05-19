# Generated by Django 3.1.3 on 2022-05-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20220513_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
        migrations.AddField(
            model_name='submission',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(),
        ),
    ]
