from django.urls import path
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.home, name='core-home'),
    path('', PostListView.as_view(), name='core-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='core-about'),
    #path('home/', views.home, name='core-home'),
]

if settings.DEBUG == True:
    urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)