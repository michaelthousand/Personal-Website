from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


# Create your models here.
class Workout(models.Model):
    MORNING = "MOR"
    AFTERNOON = "AFT"
    EVENING = "EVE"
    NIGHT = "NIT"

    TIMEDAY = [
        (MORNING, "Morning"),
        (AFTERNOON, "Afternoon"),
        (EVENING, "Evening"),
        (NIGHT, "Night")
    ]

    CARDIO = "CA"
    WEIGHTS = "WT"
    OTHER = "OT"
    HIKING = "HI"
    RUNNING = "RU"
    YOGA = "YO"
    HIT = "HT"
    SPORT = "SP"
    WALKING = "WA"

    WO_TYPE = [
        (CARDIO, "Cardio"),
        (WALKING, "Walking"),
        (RUNNING, "Running"),
        (HIKING, "Hiking"),
        (HIT, "Interval Training"),
        (WEIGHTS, "Weights"),
        (YOGA, "Yoga"),
        (SPORT, "Sport (e.g., hockey, soccer, etc.)"),
        (OTHER, "Other")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateField()
    month = ''
    year = ''
    timeday = models.CharField(verbose_name='Time of Day', max_length=3, choices=TIMEDAY)
    exercises = MultiSelectField(choices=WO_TYPE, max_choices=3, validators=[MaxValueValidator(3)], default=None)
    duration = models.PositiveIntegerField(verbose_name='Duration (in minutes)')
    cals_burned = models.PositiveIntegerField(verbose_name='Calories burned:', blank=True, null=True)
    current_weight = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True)
    id = str(user) + str(date) + str(timeday)

    def __str__(self):
        return f"Date: {self.date}, Year: {self.year}, Month: {self.month}\nTime: {self.timeday}, Type: {self.exercises}, Duration: {self.duration}, Calories Burned: {self.cals_burned}\nNotes: {self.notes}"
    

