# Generated by Django 2.2 on 2021-07-20 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobSearch_app', '0003_auto_20210719_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='post_date',
            field=models.DateField(default=None),
        ),
    ]
