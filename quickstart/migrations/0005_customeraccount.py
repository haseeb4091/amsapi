# Generated by Django 4.0.2 on 2022-03-25 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_addroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='customeraccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cnic', models.CharField(max_length=100)),
                ('phno', models.IntegerField()),
                ('role', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('room', models.CharField(max_length=100)),
                ('rent', models.IntegerField()),
                ('security', models.IntegerField()),
                ('accountno', models.IntegerField()),
                ('debt', models.IntegerField()),
            ],
        ),
    ]
