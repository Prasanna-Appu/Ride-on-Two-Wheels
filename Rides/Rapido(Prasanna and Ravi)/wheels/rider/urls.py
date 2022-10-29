from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login, name='login'),
    path('logout_user/',views.logout_user, name='logout'),
    path('signup/',views.signup, name='signup'),
    path('success/',views.success, name='success'),
    path('payment/',views.payment, name='payment'),
    path('book-a-rider/',views.bookRider,name='bookarider'),
    path('emergency-ride/',views.emergency,name='emergency'),
    path('rent-a-bike/',views.rentBike,name='rentBike'),
    path('careers/',views.careersPage,name='careers'),
]