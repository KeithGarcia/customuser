# Generated by Django 3.1 on 2020-08-26 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_auto_20200826_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='displayname',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='myuser',
            name='homepage',
            field=models.URLField(blank=True, null=True),
        ),
    ]
