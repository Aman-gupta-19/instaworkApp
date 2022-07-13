# Generated by Django 4.0.4 on 2022-07-11 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_rename_testing_teammodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammodel',
            name='age',
        ),
        migrations.RemoveField(
            model_name='teammodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='teammodel',
            name='passw',
        ),
        migrations.RemoveField(
            model_name='teammodel',
            name='sname',
        ),
        migrations.AddField(
            model_name='teammodel',
            name='fname',
            field=models.CharField(default='random', max_length=50),
        ),
        migrations.AddField(
            model_name='teammodel',
            name='lname',
            field=models.CharField(default='random', max_length=50),
        ),
        migrations.AddField(
            model_name='teammodel',
            name='pno',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teammodel',
            name='role',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='email',
            field=models.EmailField(default='random', max_length=100),
        ),
    ]