from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.index, name='login'),
    path('stream', views.stream, name='stream'),
]
