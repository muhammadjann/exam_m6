from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('blogs/', views.blogs, name='blogs'),
    path('<int:pk>/event/', views.event_detail, name='event'),
    path('<int:pk>/edit/', views.event_edit, name='edit'),
    path('<int:pk>/delete/', views.event_delete, name='delete'),
    path('create/', views.event_create, name='create'),
]
