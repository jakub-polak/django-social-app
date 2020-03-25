from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash

from accounts.forms import RegistrationForm, EditProfileForm


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
        return render(request, 'accounts/register.html', args)


@login_required
def view_profile(request):
    args = {
        'user': request.user,
    }
    return render(request, 'accounts/profile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {
            'form': form
        }
        return render(request, 'accounts/edit_profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user=form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/profile/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {
            'form': form
        }
        return render(request, 'accounts/change_password.html', args)
