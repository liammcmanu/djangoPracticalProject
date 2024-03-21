from django.shortcuts import render
from practicalApp.models import Cat, Student

def index(request):
	context_dict = {}
	context_dict['students'] = Student.objects.order_by('lastName')
	return render(request, 'practicalApp/index.html', context=context_dict)

def cats(request):
	context_dict = {}
	context_dict['cats'] = Cat.objects.order_by('name')
	return render(request, 'practicalApp/cats.html', context=context_dict)
