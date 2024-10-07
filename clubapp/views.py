from unittest import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from clubapp.admin import NotificationAdmin
from clubapp.forms import CompetitionForm, JoinPlayerForm, NotificationForm
from .models import Competition, Membership, Team


from clubapp.models import Notification
def home(request):
    teams = Team.objects.all()
    return render(request, 'home.html', {'teams': teams})

def admin_login(request):
    return render(request, 'admin_login.html')

def parent_register(request):
    return render(request, 'parent_register.html')
# def index(request):

#     template = loader.get_template('home.html')
#     context = {

#     }
#     return HttpResponse(template.render(context, request))


def logout_view(request):
    logout(request)
    return redirect('admin_login.html')

def notification_list(request):
    notifications = Notification.objects.all()
    context = {
        'notifications': notifications
    }
    return render(request, 'notification_list.html', context)
def competition_list(request):
    competitions = Competition.objects.all()
    context = {
        'competitions': competitions
    }
    return render(request, 'competition_list.html', context)
from django.shortcuts import render
from .models import Membership

def player_list(request):
    memberships = Membership.objects.select_related('team').order_by('team__name', 'player__name')
    context = {
        'memberships': memberships
    }
    return render(request, 'player_list.html', context)


def join_player(request):
    if request.method == 'POST':
        form = JoinPlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JoinPlayerForm()
    
    context = {'form': form}
    return render(request, 'join_player.html', context)


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('home')  # Redirect to the admin dashboard
        else:
            # Invalid credentials or not a superuser
            return render(request, 'admin_login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'admin_login.html')

def logout_view(request):
    logout(request)
    return redirect('home')



def add_notification(request):
    if not request.user.is_superuser:
        # Redirect to home or display an error message indicating permission denied
        return redirect('home')

    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notification')
    else:
        form = NotificationForm()

    context = {'form': form}
    return render(request, 'add_notification.html', context)

# def update_notification(request, notification_id):
#     notification = get_object_or_404(Notification, id=notification_id)

#     if request.method == 'PUT':
#         form = NotificationForm(request.PUT, instance=notification)
#         if form.is_valid():
#             form.save()
#             return redirect('notification')
#     else:
#         form = NotificationForm(instance=notification)

#     return render(request, 'update_notification.html', {'form': form, 'notification': notification})
# from django.shortcuts import redirect, reverse

# def some_view(request):
#     # Get the notification_id from somewhere
#     notification_id = 1  # Replace with your actual notification_id

#     # Redirect to the update_notification view with the notification_id
#     return redirect('update_notification', notification_id=notification_id)


def add_competition(request):
    if request.method == 'POST':
        form = CompetitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competition')
    else:
        form = CompetitionForm()
    return render(request, 'add_competition.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect, render
from .models import Notification

# def delete_notification(request, notification_id):
#     notification = get_object_or_404(Notification, id=notification_id)

#     if request.method == 'POST':
#         notification.delete()
#         return redirect('notification')  # Redirect to the desired URL after deletion

#     return render(request, 'delete_notification.html', {'notification': notification})
