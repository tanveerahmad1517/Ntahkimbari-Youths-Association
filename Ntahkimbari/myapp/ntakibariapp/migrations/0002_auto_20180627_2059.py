# Generated by Django 2.0.6 on 2018-06-28 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntakibariapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.BigIntegerField(db_index=True),
        ),
    ]
