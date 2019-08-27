# Generated by Django 2.2.4 on 2019-08-23 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t1', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='B',
            fields=[
                ('a_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Pages.A')),
                ('t2', models.CharField(max_length=20)),
            ],
            bases=('Pages.a',),
        ),
    ]