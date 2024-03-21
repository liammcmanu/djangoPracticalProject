from django.contrib import admin
from django.urls import path
from practicalApp import views
app_name = 'practicalApp'

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.index, name='index'),
	path('cats/', views.cats, name='cats'),
]
