# Generated by Django 4.0.4 on 2022-09-05 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0003_alter_game_duration_alter_game_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='duration',
            field=models.CharField(max_length=5),
        ),
    ]
