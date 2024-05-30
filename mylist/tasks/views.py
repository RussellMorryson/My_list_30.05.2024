from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import date
from .models import Task, Tag
from .forms import AddNewTask, EditTask

def index(request):    
    tasks = {}
    count = 1
    username = request.COOKIES.get('username')
    for temp in Task.objects.all():
        if str(temp.author) == str(username):
            tasks[count] = temp
            count+=1
    return render(request, 'tasks/index.html', {'tasks': tasks, 'username': request.COOKIES.get('username')})

def add(request):
    if request.method == 'POST':
        form = AddNewTask(request.POST, request.FILES)
        if form.is_valid():
            title_ = form.cleaned_data['title']
            description_ = form.cleaned_data['description']
            term_ = form.cleaned_data['term']
            tag_ = Tag.objects.filter(pk=form.cleaned_data['tag']).first()
            
            task = Task(title = title_,
                        description = description_,
                        term = term_,
                        tag = tag_,
                        status = 'Выполняется',
                        create_date = date.today(),
                        author = User.objects.filter(username=request.COOKIES.get('username')).first())
            task.save()
            return redirect('index')
    form = AddNewTask()
    return render(request, 'tasks/create.html', {'form': form, 'username': request.COOKIES.get('username')})

def edit(request):
    task_id = request.GET['pk']
    if request.method == 'POST':
        form = EditTask(request.POST)
        if form.is_valid():
            title_ = form.cleaned_data['title']
            description_ = form.cleaned_data['description']
            term_ = form.cleaned_data['term']
            tag_ = Tag.objects.filter(pk=form.cleaned_data['tag']).first()
            status = form.cleaned_data['status'] 
            
            task = Task.objects.filter(pk=task_id).first()

            if task.title != title_: task.title = title_
            if task.description != description_: task.description = description_            
            if task.term != term_: task.term = term_
            if task.tag != tag_.__str__(): task.tag = tag_.__str__()
            if task.status != status: task.status = status
            
            task.save()
        return redirect('index')
    else:        
        if task_id:
            task = Task.objects.filter(pk=task_id).first()
            form = EditTask(initial={
                'title': task.title,
                'description': task.description,
                'term': task.term,
                'tag': task.tag,
                'status': task.status})
            return render(request, 'tasks/edit.html', {'form': form, 'task': task, 'task_id': task_id, 'username': request.COOKIES.get('username')})

def delete(request):
    task_id = request.GET['pk']    
    if task_id:
        task = Task.objects.filter(pk=task_id).first()
        task.delete()
        return redirect('index')