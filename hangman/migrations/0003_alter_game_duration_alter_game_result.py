# Generated by Django 4.0.4 on 2022-09-05 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0002_player_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='result',
            field=models.CharField(max_length=4),
        ),
    ]