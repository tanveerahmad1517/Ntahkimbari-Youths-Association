# Generated by Django 2.0.6 on 2018-07-04 03:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ntakibariapp', '0015_fun'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('tag', models.CharField(choices=[('gallery', 'Gallery'), ('fun', 'Funs'), ('project', 'project')], max_length=20)),
                ('photo', models.ImageField(upload_to='photos')),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
