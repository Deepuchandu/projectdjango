# Generated by Django 3.1 on 2020-08-26 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('Address', models.CharField(max_length=50)),
                ('AccType', models.CharField(max_length=50)),
                ('PanNo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'AccDetails',
                'verbose_name_plural': 'AccDetailss',
            },
        ),
    ]
