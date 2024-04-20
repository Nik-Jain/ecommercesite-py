from django.shortcuts import render, redirect
from userauths import forms as user_forms
from django.contrib.auth import login, authenticate
from django.contrib import messages

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