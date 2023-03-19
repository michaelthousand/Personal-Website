# Generated by Django 4.1.7 on 2023-03-19 19:18

import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('workouttracker', '0005_alter_workout_cals_burned_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='cals_burned',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Calories burned:'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='duration',
            field=models.PositiveIntegerField(verbose_name='Duration (in minutes)'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercises',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('CA', 'Cardio'), ('WA', 'Walking'), ('RU', 'Running'), ('HI', 'Hiking'), ('HT', 'Interval Training'), ('WT', 'Weights'), ('YO', 'Yoga'), ('SP', 'Sport'), ('OT', 'Other')], default=None, max_length=26, validators=[django.core.validators.MaxValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='timeday',
            field=models.CharField(choices=[('MOR', 'Morning'), ('AFT', 'Afternoon'), ('EVE', 'Evening'), ('NIT', 'Night')], max_length=3, verbose_name='Time of Day'),
        ),
    ]
