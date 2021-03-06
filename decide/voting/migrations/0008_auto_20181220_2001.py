# Generated by Django 2.0 on 2018-12-20 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0007_auto_20181207_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionoption',
            name='importance',
            field=models.FloatField(choices=[(0, 'None'), (1, 'Not relevant'), (2, 'Review'), (3, 'May relevant'), (4, 'Relevant'), (5, 'Leading candidate')], default=0),
        ),
        migrations.AddField(
            model_name='questionoption',
            name='unlockquestion',
            field=models.ManyToManyField(blank=True, null=True, related_name='unlockquestion', to='voting.Question'),
        ),
        migrations.AddField(
            model_name='questionoption',
            name='weight',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='voting',
            name='isWeighted',
            field=models.BooleanField(default=False),
        ),
    ]
