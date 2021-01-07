from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name ='workoutlog-home'),
    path('about/', views.about, name='workoutlog-about'),
]
