# Generated by Django 2.0.4 on 2018-04-14 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_data', models.CharField(max_length=30)),
                ('data', models.CharField(max_length=256)),
            ],
        ),
    ]
