from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse

from accounts.forms import RegistrationForm, EditProfileForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home:home'))
    else:
        form = RegistrationForm()

        args = {
            'form': form,
        }
        return render(request, 'accounts/register.html', args)


@login_required
def view_profile(request, pk=None):
    args = {
        'user': User.objects.get(pk=pk) if pk else request.user,
    }
    return render(request, 'accounts/profile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
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
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change-password'))
    else:
        form = PasswordChangeForm(user=request.user)
        args = {
            'form': form
        }
        return render(request, 'accounts/change_password.html', args)
