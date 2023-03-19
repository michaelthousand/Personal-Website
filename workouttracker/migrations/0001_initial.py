# Generated by Django 4.1.7 on 2023-03-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('timeday', models.CharField(choices=[('MOR', 'Morning'), ('AFT', 'Afternoon'), ('EVE', 'Evening'), ('NIG', 'Night')], max_length=4)),
                ('duration', models.PositiveIntegerField()),
                ('cals_burned', models.PositiveIntegerField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('exercises', models.ManyToManyField(choices=[('CA', 'Cardio'), ('WA', 'Walking'), ('RU', 'Running'), ('HI', 'Hiking'), ('HT', 'Interval Training'), ('WT', 'Weights'), ('YO', 'Yoga'), ('HY', 'Hockey'), ('OC', 'Oculus'), ('OT', 'Other')], to='workouttracker.workout')),
            ],
        ),
    ]