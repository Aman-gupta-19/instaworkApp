# Generated by Django 4.0.4 on 2022-07-10 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_remove_testing_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='testing',
            name='age',
            field=models.IntegerField(default=20),
        ),
    ]