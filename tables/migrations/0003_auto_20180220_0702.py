# Generated by Django 2.0.2 on 2018-02-20 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_auto_20180216_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='form',
        ),
        migrations.AddField(
            model_name='table',
            name='shape',
            field=models.CharField(choices=[('Rectangle', 'Rectangle'), ('Oval', 'Oval')], default='Rectangle', max_length=50, verbose_name='Table shape'),
        ),
    ]
