# Generated by Django 3.2.7 on 2021-09-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_user_khoj_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khoj',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
