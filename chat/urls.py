from django.urls import path
from . import views
urlpatterns = [
    path("", views.chat_home, name="chat_home"),
    path("<int:pk>/", views.chat, name="chatroom"),
    path("ajax/<int:pk>/", views.ajax_load_messages, name="chatroom-ajax"),
    path("active/", views.getActiveUsers , name="active-users")
]
