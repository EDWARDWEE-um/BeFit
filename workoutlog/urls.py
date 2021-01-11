from django.urls import path
from . import views
from .views import WorkoutListView, WorkoutDetailView, WorkoutCreateView, WorkoutUpdateView, WorkoutDeleteView, UserWorkoutListView

urlpatterns = [
    path('', WorkoutListView.as_view(), name ='workoutlog-home'),
    path('user/<str:username>', UserWorkoutListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', WorkoutDetailView.as_view(), name ='workoutlog-detail'),
    path('post/new/', WorkoutCreateView.as_view(), name='workoutlog-create'),
    path('post/<int:pk>/update', WorkoutUpdateView.as_view(), name ='workoutlog-update'),
    path('post/<int:pk>/delete', WorkoutDeleteView.as_view(), name ='workoutlog-delete'),
    path('about/', views.about, name='workoutlog-about'),
]
