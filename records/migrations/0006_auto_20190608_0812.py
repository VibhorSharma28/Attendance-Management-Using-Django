# Generated by Django 2.2.1 on 2019-06-08 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_holiday'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='reason',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='detail',
            name='remark',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
