from django.shortcuts import render,redirect
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
