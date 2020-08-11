from django.shortcuts import render,redirect
from .forms import CustomregisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        register_form= CustomregisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New User Account Created,login to account"))
            return redirect('register')
  

    else:
        register_form= CustomregisterForm()
    return render(request,'register.html',{'register_form':register_form})
