from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from accounts.templates.accounts.forms import RegistrationForm


def home(request):
    numbers = range(6)
    name = 'Mr Example'

    args = {
        'name': name,
        'numbers': numbers,
    }

    return render(request, 'accounts/home.html', args)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print('POST')
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()

        args = {
            'form': form,
        }
        return render(request, '/accounts/register.html', args)


def profile(request):
    args = {
        'user': request.user,
    }
    return render(request, 'accounts/profile.html', args)
