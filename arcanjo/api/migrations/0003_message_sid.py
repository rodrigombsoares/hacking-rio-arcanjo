# Generated by Django 2.2.6 on 2019-10-19 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191019_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sid',
            field=models.CharField(default=None, max_length=300),
        ),
    ]
