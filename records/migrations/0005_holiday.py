# Generated by Django 2.2.1 on 2019-05-28 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_auto_20190524_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday_type', models.CharField(blank=True, max_length=40, null=True)),
                ('date', models.CharField(max_length=100)),
            ],
        ),
    ]
