# Generated by Django 2.2.4 on 2019-08-26 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0002_auto_20190826_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='ordering',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]