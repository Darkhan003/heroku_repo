from django.views.generic import ListView, CreateView, DetailView
from .forms import PostForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .models import Post


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'polls/add_post.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'polls/article_details.html'



def send_message(request):
    send_mail("Web programming: back end", "Salam", "200103038@stu.sdu.edu.kz",
              ["200103038@stu.sdu.edu.kz", "200103252@stu.sdu.edu.kz"], fail_silently=False,
              html_message="<b>Bold text</b><i> Italic text </i>")
    return render(request, 'polls/successfull.html')


class HomeView(ListView):
    model = Post
    template_name = 'polls/home.html'
