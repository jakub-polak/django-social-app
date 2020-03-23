from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


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
        form = UserCreationForm(request.POST)
        print('POST')
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = UserCreationForm()

        args = {
            'form': form,
        }
        return render(request, 'accounts/register.html', args)
