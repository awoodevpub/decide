# Generated by Django 2.0 on 2018-12-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0006_auto_20181207_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='votings',
        ),
        migrations.AddField(
            model_name='voting',
            name='questions',
            field=models.ManyToManyField(related_name='votings', to='voting.Question'),
        ),
    ]
