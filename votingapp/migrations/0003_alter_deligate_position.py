# Generated by Django 5.1.7 on 2025-03-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingapp', '0002_alter_voter_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deligate',
            name='position',
            field=models.CharField(max_length=100),
        ),
    ]
