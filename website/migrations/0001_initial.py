# Generated by Django 4.0.1 on 2022-01-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=25)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
