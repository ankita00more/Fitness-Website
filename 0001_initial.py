# Generated by Django 3.2.5 on 2021-07-29 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=196)),
                ('subject', models.CharField(max_length=196)),
                ('message', models.TextField()),
            ],
        ),
    ]
