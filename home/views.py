from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from home.forms import HomeForm
from home.models import Post, Friend


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created_date')
        users = User.objects.exclude(id=request.user.id)
        try:
            friends = Friend.objects.get(current_user=request.user).users.all()
        except ObjectDoesNotExist:
            friends = []

        return render(
            request,
            self.template_name,
            {
                'form': form,
                'posts': posts,
                'users': users,
                'friends': friends,
            }
        )

    def post(self, request, *args, **kwargs):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home:home')


def change_follow_state(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'follow':
        Friend.follow(request.user, friend)
    elif operation == 'unfollow':
        Friend.unfollow(request.user, friend)
    return redirect('home:home')
