from datetime import datetime
from .models import Workout
# Functions for Workout Tracker App

# Check for the average workout duration
def get_duration(user):
    workouts = list(user.workout_set.all())
    total_dur = 0
    num_workout = len(workouts)

    for workout in workouts:
        total_dur = total_dur + workout.duration
    
    if num_workout == 0:
        avg_dur = 0
    else:
        avg_dur = total_dur / num_workout
    
    return int(avg_dur)

# Checks for the number of workout and calories burned for the current month
def workouts_this_month(user, month):
    workouts = list(user.workout_set.filter(date__month=month))
    num_workout = len(workouts)
    total_calories = 0
    for workout in workouts:
        if workout.cals_burned == None:
            total_calories += 0
        else:
            total_calories += workout.cals_burned
    return num_workout, total_calories

def get_weightloss(user):
    workouts = Workout.objects.filter(user=user).order_by('date')
    if not workouts:
        return 0
    first_entry = workouts.first().current_weight
    latest_entry = workouts.last().current_weight
    if first_entry == None or latest_entry == None:
        change = 0
    else:
        change = latest_entry - first_entry
    return change
    

