from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignupForm, UserForm, ProfileForm
from .models import Profile
from django.urls import reverse
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/chat/')

    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {"form":form})

def profile(request):
    pro = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {"pro":pro})

def edit_profile(request):
    pro = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = UserForm(request.POST, instance= request.user)
        profform = ProfileForm(request.POST, instance= pro)
        if userform.is_valid() and profform.is_valid():
            username.save()
            myp = profform.save(commit=False)
            myp.user = request.user
            myp.save()
            return redirect(reverse('chat:chat_home'))
    else:
        userform = UserForm(instance=request.user)
        profform = ProfileForm(instance=pro)
    return render(request, 'accounts/profile_edit.html', {
    "uform": userform,
    "profform": profform,
    "pro": pro
    })
