# backend/urls.py
import sys
sys.path.append('to-do-django/backend_todo/todo/')
from django.contrib import admin
from django.urls import path, include                
from rest_framework import routers      
from todo import views              
                                            


sys.path.append('../')

router = routers.DefaultRouter()                     
router.register(r'todos', views.TodoView, 'todo')     

urlpatterns = [
    path('admin/', admin.site.urls),         path('api/', include(router.urls))                # add this
]


