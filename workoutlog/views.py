from django.shortcuts import render
from .models import Workout
posts = [## Dummy data
    {
    'name':'Push Up',
    'sets':'5',
    'reps':'8',
    'date':'August 27, 2018'

    },
    {
    'name':'Pull Up',
    'sets':'5',
    'reps':'8',
    'date':'August 27, 2018'

}
]


# Create your views here.
def home(request):
    context = {'posts': Workout.objects.all()}
    return render(request,'workoutlog/home.html',context)

def about(request):
    return render(request,'workoutlog/about.html',{'title':'About'})