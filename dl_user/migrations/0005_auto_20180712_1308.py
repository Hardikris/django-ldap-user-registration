# Generated by Django 2.0.6 on 2018-07-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dl_user', '0004_auto_20180712_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistrationrecord',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userregistrationrecord',
            name='organization',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
