from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
# Save Users
# Save Workout name
# Save Workout amount
# User details

class Workout(models.Model):
    workoutname = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    #1 to many relationship btw user and workout
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.workoutname

    def get_absolute_url(self):
        return reverse('workoutlog-detail',kwargs={'pk': self.pk})
