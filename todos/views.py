from django.shortcuts import render, redirect, render_to_response
from django.http.response import HttpResponse
from .models import Todo

def index(request):
	todos = Todo.objects.all()[:10]
	context = {
	'todos' : todos
	}
	return render(request,'index.html',context)

def details(request,id):
	todo = Todo.objects.get(id = id)
	context = {
	'todo' : todo
	}
	return render(request,'details.html',context)

def add(request):
	if(request.method == 'POST'):
		title = request.POST['title']
		text = request.POST['text']
		status = request.POST['status']
		todo = Todo(title = title, text = text, status = status)
		todo.save()
		return redirect('/todos')
	else:
		return render(request,'add.html')

def edit(request,id):
	todo = Todo.objects.get(id = id)
	context = {
	'todo' : todo
	}
	if(request.method == 'POST'):
		if(request.POST['title'] != ''):
			todo.title = request.POST['title']
		if(request.POST['text'] != ''):
			todo.text = request.POST['text']
		todo.status = request.POST['status']
		todo.err_flag=1
		todo.save()
		return redirect('/todos')
	else:
		return render(request,'edit.html',context)

def delete(request,id):
	todo = Todo.objects.get(id = id)
	context = {
	'todo' : todo
	}
	todo.delete()
	return redirect('/todos')