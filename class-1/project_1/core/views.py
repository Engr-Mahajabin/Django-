from django.shortcuts import render,redirect,get_object_or_404
from .models import student
from .forms import studentForm
# Create your views here.
def index(request): 
    model = student.objects.all()
    return render(request,'index.html',{'model':model})

def add_student(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else: 
        form = studentForm()
    return render(request,'add_student.html', {'form':form})

def update_student(request,id):
    stu = get_object_or_404(student,id=id)
    form = studentForm (request.POST or None, instance=stu)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'update_student.html',{'form':form})

def delete_student(request,id):
    stu = get_object_or_404(student,id=id)
    if request.method == 'POST':
        stu.delete()
        return redirect ('index')
    return render(request,'delete_student.html',{'stu':stu})