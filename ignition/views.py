from django.shortcuts import render, redirect
from .models import Task
from .forms import Task_form
from rest_framework.views import APIView
from .serializers import ToDoSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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



class view_api(APIView):

    def get(self, request):
        todos = Task.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = ToDoSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class delete_api(APIView):

    def delete(self, request, pk):
        todo = get_object_or_404(Task, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

