from django.urls import path
from . import views
from .views import contact, about, privacy, terms

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('privacy', views.privacy, name='privacy'),
    path('terms', views.terms, name='terms'),
    path('signup/', views.signup, name='signup')
]