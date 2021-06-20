from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from accounts.models import Profile
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from .models import User, Message
from django.db.models import Q
import json


def get_all_logged_in_users():
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))
    return Profile.objects.filter(id__in=uid_list)


def chat(request, pk:int):
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(
        Q(receiver=request.user, sender=other_user)
    )
    messages.update(seen=True)
    messages = messages | Message.objects.filter(Q(receiver=other_user, sender=request.user) )
    other_user = Profile.objects.get(user= other_user)
    return render(request, "chat/chat.html", {
        "other_user": other_user,
        "messages": messages,
     })
     # "pro":get_all_logged_in_users(),

def chat_home(request):
    user = Profile.objects.get(user=request.user)
    active = get_all_logged_in_users()
    return render(request, 'chat/chat_home.html', {"user":user, "pro":active})

def ajax_load_messages(request, pk:int):
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(seen=False).filter(
         Q(receiver=request.user, sender=other_user)
         )
    message_list = [{
     "sender": message.sender.username,
     "message": message.message,
     "sent": message.sender == request.user
    } for message in messages]
    messages.update(seen=True)

    if request.method == "POST":
         message = json.loads(request.body)
         m = Message.objects.create(receiver=other_user, sender=request.user, message=message)
         message_list.append({
             "sender": request.user.username,
             "message": m.message,
             "sent": True,
             })
    return JsonResponse(message_list, safe=False)

def getActiveUsers(request):
    activeUsersProfiles = get_all_logged_in_users()
    act_users = [{
    "id": u.user.id,
    "user": u.user.username,
    "img" : u.img.url

    } for u in activeUsersProfiles if u.user.id != request.user.id]

    return JsonResponse(act_users, safe=False)
