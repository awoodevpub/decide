# Generated by Django 2.0 on 2019-01-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0008_auto_20181220_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='questions',
            field=models.ManyToManyField(related_name='voting', to='voting.Question'),
        ),
    ]
