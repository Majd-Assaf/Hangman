# Generated by Django 4.0.4 on 2022-09-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0004_alter_game_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateTimeField(),
        ),
    ]