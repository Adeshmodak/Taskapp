from django.shortcuts import render,redirect
from django.http import HttpResponse
from mylist_app.models import Tasklist
from mylist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def mylist(request):
    if request.method=="POST":
        form=TaskForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manage=request.user
            instance.save()
        messages.success(request,("New Task Added!"))    
        return redirect('mylist')    

    else:
      all_tasks= Tasklist.objects.filter(manage = request.user)
      paginator=Paginator(all_tasks,3)
      page = request.GET.get('pg')
      all_tasks=paginator.get_page(page)
      return render(request,'myapp.html',{'all_tasks':all_tasks})

def delete_task(request , task_id):
    task=Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request,("Access Restricted"))        
    return redirect('mylist')

@login_required
def edit_task(request , task_id):
    if request.method=="POST":
        task=Tasklist.objects.get(pk=task_id)
        form=TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()

        messages.success(request,("Task Edited!"))    
        return redirect('mylist')    

    else:
        task_obj= Tasklist.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})

@login_required
def complete_task(request , task_id):
    task=Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done=True
        task.save()
    else:
        messages.error(request,("Access Restricted"))    
    return redirect('mylist')        

def pending_task(request , task_id):
    task=Tasklist.objects.get(pk=task_id)
    task.done=False
    task.save()
    return redirect('mylist')       

def index(request):
    context = {
        'index_text':"Welcome from index page"
    }
    return render(request,'index.html',context)     

def about(request):
    context = {
        'about_text':"Welcome from about page"
    }
    return render(request,'aboutus.html',context) 

def contact(request):
    context = {
        'contact_text':"Welcome from contact page"
    }
    return render(request,'contactus.html',context)    