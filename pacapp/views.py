from django.shortcuts import render
from models import Pacs
from models import Students
from models import PastoralNotes

# Create your views here.


def mypacs(request):
    mypacs = Pacs.objects.all()
    context = {'mypacs': mypacs}
    return render(request, 'pacs.html', context)

def mystudents(request):
    mystudents = Students.objects.all()
    context = {'mystudents': mystudents}
    return render(request, 'students.html', context)

def mypastoralnotes (request):
    mypastoralnotes = PastoralNotes.objects.all()
    context = {'mypastoralnotes': mypastoralnotes}
    return render(request, 'pastoralnotes.html', context)
