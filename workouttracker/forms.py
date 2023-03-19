from django import forms
from .models import Workout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        exclude = ('user',)


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False, max_length=20)
    last_name = forms.CharField(required=False, max_length=20)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        # Validate email to ensure it's properly formatted and not already in use by another user
        if not email:
            raise forms.ValidationError("Email is required.")
        elif User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name:
            return first_name.strip()
        return ''

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name:
            return last_name.strip()
        return ''
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user