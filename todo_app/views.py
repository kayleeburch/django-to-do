import re
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponseRedirect
from .models import Todo
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AppUser as User
from .models import Todo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/') 
@csrf_exempt
def index(request):
    return render(request, 'index.html', {'user_email': request.user.email})
    
@login_required(login_url='/login/')   
def all_todos(request):
    items = Todo.objects.filter(user_id=request.user.id)
    print(request.user.id)
    return render(request, 'all_todo.html', {'items': items, 'user': request.user})


@csrf_exempt
def signup(request):
    print('trying to signup')
    if request.method == 'GET':
            return render(request, 'sign_up.html')
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            User.objects.create_user(username=body['email'], password=body['password'], email=body['email'])
            return JsonResponse({'success': True})
        except Exception as e:
            print('oops!')
            print(str(e))
            return JsonResponse({'success': False})
        
@csrf_exempt     
def log_in(request):
    print('trying to login')
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        body = json.loads(request.body)
        email = body['email']
        password = body['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                try:
                    login(request,user)
                    print('logged in!')
                    return JsonResponse({'Success': True})
                except Exception as e:
                    return JsonResponse({'Success': False, 'reason': 'login failed'})
            else:
                return JsonResponse({'Success': False, 'reason': 'account disabled'})
        else:
            return JsonResponse({'Success': False, 'reason': 'user does not exist'})

def log_out(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/')
   
@csrf_exempt
def add_item(request):
    print('function reached')
    if request.method == 'POST':
        body = json.loads(request.body)
        new_list_item = Todo(title=body['title'], body=body['body'], user_id=request.user.id)
        new_list_item.save()
        return JsonResponse({'success': True})
    else:
        print('get request')
        return render(request, 'add_item.html')
    
def get_details(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo_info = Todo.objects.all()
    
    data = {'todo': todo, 'todo_info': todo_info}
    # return HttpResponse(f"You are looking at: {todo}")
    return render(request, 'todo_details.html', data)

@csrf_exempt
def update_item(request, todo_id):
    print('function reached')
    if request.method == 'POST':
        body = json.loads(request.body)
        todo = Todo.objects.get(id = todo_id)
        todo.title=body['title']
        todo.body=body['body']
        todo.save()
        return JsonResponse({'success': True})
    else:
        print('get request')
        todo = Todo.objects.get(id = todo_id)
        return render(request, 'update_item.html', {'todo': todo})
    
def delete_view(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    if request.method == 'POST':
        todo.delete()
        return HttpResponseRedirect("/all_todos/")
    return render(request, "delete_view.html")