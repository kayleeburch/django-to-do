from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .models import Todo
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def index(request):
    items = Todo.objects.all()
    return render(request, 'index.html', {'items': items})
    
@csrf_exempt
def add_item(request):
    print('function reached')
    if request.method == 'POST':
        body = json.loads(request.body)
        new_list_item = Todo(title=body['title'], body=body['body'])
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
        return HttpResponseRedirect("/")
    return render(request, "delete_view.html")