from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from home.forms import HomeForm
from home.models import Post


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created_date')
        return render(request, self.template_name, {'form': form, 'posts': posts})

    def post(self, request, *args, **kwargs):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home:home')
