# Generated by Django 2.2.1 on 2019-05-24 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_remove_detail_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='entry_time',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='exit_time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]