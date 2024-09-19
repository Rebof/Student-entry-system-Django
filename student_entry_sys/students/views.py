from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm

# API ViewSet
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# HTML views 
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_form_view(request, student=None): #combining the create and update for now.
    form = StudentForm(request.POST or None, instance=student) #if post data is populated(works)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form})

def student_create(request):
    return student_form_view(request)

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return student_form_view(request, student)

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return redirect('student_list')  