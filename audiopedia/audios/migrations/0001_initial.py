# Generated by Django 2.1.4 on 2020-09-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True)),
                ('language', models.TextField(blank=True)),
                ('category', models.TextField(blank=True)),
            ],
        ),
    ]