# Generated by Django 4.0.6 on 2022-08-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_cupapp', '0005_ranking'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranking',
            name='rank',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
