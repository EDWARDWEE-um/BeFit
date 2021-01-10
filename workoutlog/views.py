from django.shortcuts import render
from .models import Workout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def home(request):
    context = {'posts': Workout.objects.all()}
    return render(request,'workoutlog/home.html',context)



class WorkoutListView(ListView):
    model = Workout
    template_name = 'workoutlog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # order the post date
    # <app>/<model>_<viewtype.html>

class WorkoutDetailView(DetailView):
    model = Workout


class WorkoutCreateView(LoginRequiredMixin,CreateView):
    model = Workout
    fields = ['workoutname','sets','reps']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class WorkoutUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Workout
    fields = ['workoutname','sets','reps']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):## prevents other users from updating other user's post
        Workout = self.get_object()
        if self.request.user == Workout.author:
            return True
        return False

class WorkoutDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    # user must login and author of the post
    model = Workout
    success_url = '/'
    def test_func(self):## prevents other users from del other user's post
        Workout = self.get_object()
        if self.request.user == Workout.author:
            return True
        return False

def about(request):
    return render(request,'workoutlog/about.html',{'title':'About'})
