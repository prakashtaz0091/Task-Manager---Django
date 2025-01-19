from django.shortcuts import render, redirect
from . import forms
from .models import Task
from django.db.models import Q


def search_task(request):
    search_keyword = request.GET.get('search')
    
    
    request.session['search_keyword'] = search_keyword
    return redirect('home')
    
    
    

def delete_task(request, pk):
    # print(pk)
    #retrieve the task to be deleted from db
    task_to_be_deleted = Task.objects.get(id=pk)
    task_to_be_deleted.delete()
    
    return redirect('home')

def update_task(request, pk):
    
    
    if request.method == "POST":
        form = forms.TaskForm(request.POST)
        
        if form.is_valid():
            form.save()
        
        return redirect('home')
    
    
    # retrive the task to be updated from db    
    task_to_be_updated = Task.objects.get(id=pk)
    
    #fill the form with the retrived task i.e. task to be updated
    update_form = forms.TaskForm(instance=task_to_be_updated)
    tasks = Task.objects.all().order_by('-created_at') # retrive all tasks to show
    
    context = {
        'form': update_form,
        'tasks': tasks
    }
    
    
    return render(request, 'app/update.html', context)


def home(request):
    
    #using model form - shortcut way
    if request.method == "POST":
        form = forms.TaskForm(request.POST)
        
        if form.is_valid():
            form.save()
        
        return redirect('home')
    
    #using manual method
    # if request.method == "POST":
    #     form_data = request.POST
    #     task_name = form_data['name']
    #     task_desc = form_data['desc']
    #     task_deadline = form_data['deadline']
        
    #     Task.objects.create(name=task_name, desc=task_desc, deadline=task_deadline)
    #     # task = Task()
    #     # task.name = task_name
    #     # task.desc = task_desc
    #     # task.deadline = task_deadline
    #     # task.save()
        
        
    #     return redirect('home')
    
        
    
    form = forms.TaskForm()
    
    search_keyword = request.session.get('search_keyword')
    if search_keyword:
        filtered_tasks = Task.objects.filter(
                        Q(name__icontains=search_keyword) |
                        Q(desc__icontains=search_keyword) 
                ).order_by('-created_at')
        tasks = filtered_tasks
        del request.session['search_keyword']
        
    else:
        tasks = Task.objects.all().order_by('-created_at')
    
    context = {
        'form': form,
        'tasks': tasks
    }
    
    
    return render(request, 'app/home.html', context)