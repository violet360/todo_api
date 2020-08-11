from django.shortcuts import render, redirect
from .models import Task
from .forms import Task_form

# Create your views here.

def display_list(request):
	if request.method == 'POST':
		form = Task_form(request.POST)
		if(form.is_valid()):
			form.save()

		return redirect('display_list')


	objs = Task.objects.all()
	for obj in objs:
		print(obj.pk)
	form = Task_form()
	return render(request,'ignition/index.html',{'tasks': objs, 'form':form})


def del_task(request, pk):
	obj = Task.objects.get(pk = pk)
	obj.delete()
	return redirect('display_list')

