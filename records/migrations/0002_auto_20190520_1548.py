# Generated by Django 2.2.1 on 2019-05-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='entry_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='detail',
            name='exit_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='detail',
            name='work_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='record',
            name='staff_name',
            field=models.CharField(max_length=100),
        ),
    ]
