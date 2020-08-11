from django.urls import path
from . import views
from .views import view_api, delete_api 
urlpatterns = [
	path('', views.display_list, name = 'display_list'),
	path('api/', view_api.as_view()),
	path('api/<int:pk>/', delete_api.as_view()),
	path('<int:pk>/', views.del_task, name = 'del_task')
]