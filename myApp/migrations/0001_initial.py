# Generated by Django 4.0.4 on 2022-07-09 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200)),
                ('passw', models.CharField(max_length=200)),
                ('age', models.PositiveBigIntegerField(max_length=100)),
            ],
        ),
    ]
