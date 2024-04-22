from django.shortcuts import render, redirect
from userauths import forms as user_forms
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings

User = settings.AUTH_USER_MODEL

def register_view(request):
    
    if request.method == "POST":
        form = user_forms.UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 
                             message=f"Hello {username}, Your account is created successfully!")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("core:index")

    else:
        form=user_forms.UserRegisterForm()

    context = {'form':form}

    return render(request, "userauths/sign-up.html", context)


def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already Logged In!")
        return redirect('core:index')
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            if user:
                user = authenticate(request, email=email, password=password)
                if user:
                    login(request, user)
                    return redirect('core:index')
                else:
                    messages.warning(request, "User does not exists, create an account")
        except Exception:
            messages.warning(request, f"User with {email} does not exists.")
        
    return render(request, 'userauths/sign-in.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You are logged out successfully!")
    return redirect('userauths:sign-in')
