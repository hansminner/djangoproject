from django.shortcuts import render

# Create your views here.

def student(request):
     list = [{id: 1, 'name': 'Jack'}, {id: 2, 'name': 'Rose'}]
     return render(request, 'student.html', {'students': list})
 

