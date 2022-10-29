from django.urls import path
from . import views
urlpatterns = [
    path('',views.homePage, name='home'),
    path('about/',views.aboutPage, name='about'),
    path('services/',views.servicesPage, name='services'),
    path('careers/',views.careersPage, name='careers'),
    path('contact/',views.contactPage, name='contact'),
]