from django.urls import path
from . import views

urlpatterns = [
	path('', views.display_list, name = 'display_list'),
	path('<int:pk>/', views.del_task, name = 'del_task')
	# path('')
	# path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
]