from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import like_post
from django.urls import path
from .views import edit_post, post_detail, post_list

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add/', views.add_post, name='add_post'),
    path('post/<str:pk>/', post_detail, name='post_detail'),
    path('edit/<str:pk>/', views.edit_post, name='edit_post'),
    path('delete/<str:pk>/', views.delete_post, name='delete_post'), 
    path('like/<str:pk>/', views.like_post, name='like_post'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)