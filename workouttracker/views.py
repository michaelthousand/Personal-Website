from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Workout
from .forms import WorkoutForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from workouttracker.utils import get_duration, workouts_this_month, get_weightloss
from datetime import datetime
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.utils.html import escape, strip_tags
from django.utils import timezone


# Testing

from django.core.exceptions import ValidationError


User = get_user_model()

# Create your views here.
def workouthome(request):
    return render(request, 'workouttracker/workouthome.html')

# List of all workouts
class WorkoutList(LoginRequiredMixin, ListView):
    model = Workout
    template_name = "workouttracker/workouts.html"
    context_object_name = 'workouts'
    ordering = ['-date']
    paginate_by = 10
    empty_message = 'No data available'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

# Allows the user to add new workouts
class AddWorkout(LoginRequiredMixin, CreateView):
    model = Workout
    form_class = WorkoutForm
    template_name = "workouttracker/add_workout.html"
    success_url = reverse_lazy('workoutlist')

    def form_valid(self, form):
        # Check that the workout date is in the past
        workout_date = form.cleaned_data['date']
        if workout_date > timezone.now().date():
            form.add_error('date', 'Workout date cannot be in the future')

        # Sanitize user input data to prevent XSS attacks
        form.instance.date = escape(strip_tags(form.instance.date))
        form.instance.duration = escape(strip_tags(form.instance.duration))
        if form.instance.cals_burned != None:
            form.instance.cals_burned = escape(strip_tags(form.instance.cals_burned))
        if form.instance.current_weight != None:
            form.instance.current_weight = escape(strip_tags(form.instance.current_weight))
        form.instance.notes = escape(strip_tags(form.instance.notes))

        # Check if there are any other validation errors on the form
        if form.errors:
            return self.form_invalid(form)
        
        form.instance.user = self.request.user
        return super().form_valid(form)

# Update workout
class UpdateWorkout(LoginRequiredMixin, UpdateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'workouttracker/update_workout.html'
    success_url = reverse_lazy('workoutlist')

    def get_object(self, queryset=None):
        id = self.kwargs['id']
        return self.model.objects.get(id=id)
    
    def form_valid(self, form):
        # Check that the workout date is in the past
        workout_date = form.cleaned_data['date']
        if workout_date > timezone.now().date():
            form.add_error('date', 'Workout date cannot be in the future')
        
        # Sanitize user input data to prevent XSS attacks
        form.instance.date = escape(strip_tags(form.instance.date))
        form.instance.duration = escape(strip_tags(form.instance.duration))
        if form.instance.cals_burned != None:
            form.instance.cals_burned = escape(strip_tags(form.instance.cals_burned))
        if form.instance.current_weight != None:
            form.instance.current_weight = escape(strip_tags(form.instance.current_weight))
        form.instance.notes = escape(strip_tags(form.instance.notes))

        # Check if there are any other validation errors on the form
        if form.errors:
            return self.form_invalid(form)
        
        form.instance.user = self.request.user
        return super().form_valid(form)

# Delete workout
class DeleteWorkout(LoginRequiredMixin, DeleteView):
    model = Workout
    template_name = 'workouttracker/delete_workout.html'
    success_url = reverse_lazy('workoutlist')

    def get_object(self, queryset=None):
        id = self.kwargs['id']
        return self.model.objects.get(id=id)

# User signup
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    

# User logout
@login_required
def logout_view(request):
    logout(request)
    return redirect("workouthome")

# User Profile
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        month = datetime.now().month
        avg_dur = get_duration(user)
        month_stats = workouts_this_month(user, month)
        weight_loss = get_weightloss(user)
        context['user'] = user
        context['avg_dur'] = avg_dur
        context['num_for_month'] = month_stats[0]
        context['cals_for_month'] = month_stats[1]
        context['weight_loss'] = weight_loss
        return context


# Will need to add more, but this will be where the functions for the stats pageg are returned
def stats_view(request):
    user = request.user
    avg_dur = get_duration(user)
    context = {'avg_dur': avg_dur}
    return render(request, 'workouttracker/view_stats.html', context)




# Testing
