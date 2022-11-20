from ast import Import
from django.shortcuts import render
from .forms import StudentRegistration
from django.shortcuts import redirect
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)


# Create your views here.
from django.http import HttpResponse
from attendance_app.models import Students


def student(request):
    #return HttpResponse ("<h1>Heelo kutta</h1>")
    if  request.method=="POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            First_name= request.POST.get('First_name')
            Last_name= request.POST.get('Last_name')
            #print('Agree:', fm.cleaned_data['agree'])

            en = Students(First_name=First_name,Last_name=Last_name, attendance=False)
            en.save()
            fm= StudentRegistration()
    else:
        fm = StudentRegistration()
    stud=Students.objects.all()
    n='Data Inserted'
    return render(request,"student.html",{'n':n})

def teacherform(request):
    fm = StudentRegistration()
    stud = Students.objects.all()
    return render(request, 'teacher.html', {'form': fm , 'stu':stud})
    #return HttpResponse(request)

def delete(request, id):
    stud= Students.objects.get(id=id)
    stud.delete()
    return redirect("/teacherform")

def edit(request, id):
    if request.method == 'POST':
        pi= Students.objects.get(pk=id)
        fm= StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        else:
            pi= Students.objects.get(pk=id)
            fm= StudentRegistration(instance=pi)
            return render(request, 'edit.html', {'id':id})

# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Students, id = id)
 
    # pass the object as instance in form
    form = StudentRegistration(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/teacherform")
        #return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)
