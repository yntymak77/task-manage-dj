from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from dailytask.views import task_done, task_detail

# @requiresCard()
@login_required(login_url="/login")
def index(request):
    user = request.user
    if user.userprofile.daily_task == False:
        return render(request, 'home.html')
    elif user.userprofile.daily_task_done == True:
        user = request.user
        task_id = user.userprofile.daily_task
        return task_done(request, pk=task_id)
    else:
        user = request.user
        task_id = user.userprofile.daily_task
        return task_detail(request, pk=task_id)


def logout_view(request):
    logout(request)
    return redirect('/login')
