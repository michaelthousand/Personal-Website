from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views
from .views import *

urlpatterns = [
    path('', views.workouthome, name="workouthome"),
    path('workouts/', views.WorkoutList.as_view(), name='workoutlist'),
    path('workout/create', views.AddWorkout.as_view(), name='addworkout'),
    path('workout/<str:id>/update/', views.UpdateWorkout.as_view(), name='updateworkout'),
    path('workout/<str:id>/delete/', views.DeleteWorkout.as_view(), name='deleteworkout'),
    # Auth link
    path('account/', include("django.contrib.auth.urls")),
    # Login link
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Signup link
    path('signup/', views.SignUp.as_view(),  name='signup'),
    # Logout link
    path('logout/', views.logout_view, name='logout'),
    # Profile link
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
]