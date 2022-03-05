from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
import datetime
from datetime import datetime, timedelta
from dailytask.models import TaskCompletedTimes, Task


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    daily_task = models.IntegerField(default=0)
    daily_task_done = models.BooleanField(default=False)
    daily_task_done_time = models.DateTimeField(default=datetime.now() - timedelta(days=2))
    current_step = models.IntegerField(default=0)
    timezone = models.CharField(max_length=255, default='0', blank=True, null=True, )
    completed_at = models.TextField(null=True, default="", blank=True)
    my_tasks_completed = models.IntegerField(default=0)
    number_of_tasks = models.IntegerField(default=0)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


def update_task(sender, user, request, **kwargs):
    user = request.user
    current_date = datetime.now()
    if user.userprofile.daily_task_done_time.day != current_date.day:
        user.userprofile.daily_task_done = False
        user.userprofile.daily_task = 0
        user.userprofile.current_step = 0
        user.userprofile.save()


def update_users_tasks_completed(sender, user, request, **kwargs):
    user = request.user
    all_tasks = Task.objects.filter(creator=user)
    all_tasks_count = 0
    for task in all_tasks:
        the_task = TaskCompletedTimes.objects.filter(task_completed=task)
        completed_times = the_task.count()
        all_tasks_count += completed_times

    user.userprofile.my_tasks_completed = all_tasks_count
    user.userprofile.save()

user_logged_in.connect(update_task, sender=User)
user_logged_in.connect(update_users_tasks_completed, sender=User)
