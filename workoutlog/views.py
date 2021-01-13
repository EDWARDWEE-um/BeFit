from django.shortcuts import render , get_object_or_404
from .models import Workout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.
def home(self , request):
    context = {'posts': self.Workout.objects.all()}
    return render(request,'workoutlog/home.html',context)



class WorkoutListView(ListView):
    model = Workout
    template_name = 'workoutlog/home.html'
    context_object_name = 'posts'
    paginate_by = 5 # page


class UserWorkoutListView(LoginRequiredMixin,ListView):
    model = Workout
    template_name = 'workoutlog/user_home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # order the post date
    # <app>/<model>_<viewtype.html>
    paginate_by = 5 # page

    def get_queryset(self):
        return self.Workout.objects.filter(user=self.request.user).order_by('-date_posted')



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
