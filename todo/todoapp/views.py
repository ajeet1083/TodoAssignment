from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm, UserRegistrationForm
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def todo(request):
    todo = Todo.objects.filter(user = request.user)
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
                
            todo = Todo(
                user = request.user,
                title = request.POST['title'],
                is_finished = finished
            )
            todo.save()
            messages.success(request, f'To do added successfully from {request.user}')
        return redirect('todo')
    else:
        form = TodoForm()
    context = {'todos' : todo, 'form' : form}
    return render(request, 'dashboard/todo.html', context)

def update_todo(request, id):
    todo = Todo.objects.get(id = id)
    if todo.is_finished:
        todo.is_finished = False
    else:
         todo.is_finished = True
    todo.save()
    return redirect('todo')

def delete_todo(request, id):
    Todo.objects.get(id = id).delete()
    return redirect('todo')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account is created for {username} !!')
            return redirect('login')

    else:       
        form = UserRegistrationForm()
    contex = {
        'form' : form
    }
    return render(request, 'dashboard/register.html', contex)

@login_required(login_url = 'login')
def profile(request):
    
    todo = Todo.objects.filter(is_finished = False, user = request.user)
    
    if len(todo) == 0 :
        todo_done = True
    else:
        todo_done = False
        
    context = {
        'todos' : todo,
        'todo_done' : todo_done,
    }
    return render(request, 'dashboard/profile.html', context)
