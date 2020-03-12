from blog.views import SinglePostView
from django.urls import path
from django.conf.urls import url
from blog import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    path('posty', views.PostView, name='post_list'),
    path('post/<int:pk>', SinglePostView.as_view(), name='single_post'),
    # path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]