from msilib.schema import Class
from tkinter import Entry
from unicodedata import name
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from .models import TeamModel
from .forms import TeamForm

# Create your views here.

def ListPage(request):
    team_list = TeamModel.objects.all()
    count = TeamModel.objects.count()
    return render(request, "ListPage.html", {'team_list': team_list, 'count': count})

def AddPage(request):
    team_list = TeamModel.objects.all()
    if request.method == 'POST':
        form = TeamForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, "ListPage.html", {'team_list':team_list})
    else:
        return render(request, "AddPage.html")

def EditPage(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        record = TeamModel.objects.get(id=id)
        record.fname = request.POST.get('fname')
        record.lname = request.POST.get('lname')
        record.pno = request.POST.get('pno')
        record.email = request.POST.get('email')
        record.role = request.POST.get('role')
        new_values = TeamForm(request.POST or None)
        if new_values.is_valid():    
            record.save ()
        team_list = TeamModel.objects.all()
        count = TeamModel.objects.count()
        return render(request, "ListPage.html", {'team_list': team_list, 'count': count})
    elif request.method == 'GET':
            id = request.GET['id']
            team_list = TeamModel.objects.get(id=id)
            return render(request, "EditPage.html", {'team_list':team_list, 'id':id})
    else:
        return HttpResponse('Something went wronf please try again!')

def DelRec(request):
    id = request.GET['id']
    TeamModel.objects.get(id=id).delete()
    return render(request, "DelRec.html")
    
