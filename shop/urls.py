from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='SHopeHome'),
    path('about', views.about, name=''),
    path('contact', views.contact, name='ContactUs'),
    path('tracker', views.tracker, name='TrackOrder'),
    path('search', views.search, name='Search'),
    path('product', views.product, name='ProductView'),
    path('checkout', views.checkout, name='Checkout'),
]
