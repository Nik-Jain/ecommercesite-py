from django.shortcuts import render
from userauths import forms as user_forms

def register_view(request):
    
    if request.method == "POST":
        form = user_forms.UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()

    else:
        form=user_forms.UserRegisterForm()

    context = {'form':form}

    return render(request, "userauths/sign-up.html", context)