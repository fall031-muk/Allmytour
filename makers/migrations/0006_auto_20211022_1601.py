# Generated by Django 3.2.8 on 2021-10-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makers', '0005_alter_draftmaker_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draftmaker_drafttour',
            name='limit_load',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='draftmaker_drafttour',
            name='limit_people',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
