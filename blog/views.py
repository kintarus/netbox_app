from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
import django.contrib.auth.decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.conf.urls.static import static
from django.db import models
from .models import Post, Comment
from django.utils import timezone
from .forms import CommentForm

def PostView(request):
    posty = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posty':posty})

class SinglePostView(View):
    def get(self, request, pk):
        single_post = get_object_or_404(Post, id=pk)
        comments = Comment.objects.all()
        posty = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        context = {
            'single_post':single_post,
            'posty':posty,
            'comments':comments,
        }
        return TemplateResponse(request, 'single_post.html', context=context)


# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         form = CommentForm()
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('single_post', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'add_comment_to_post.html', {'form':form})

def JobOfferView(request):
    oferty = JobOffer.objects.filter(published_date__lte=timezone.now().order_by('published_date'))
    return render(request, 'oferty_pracy.html', {'oferty':oferty})
