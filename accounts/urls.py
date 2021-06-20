from django.urls import path
from . import views
urlpatterns = [
    path('', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

]
