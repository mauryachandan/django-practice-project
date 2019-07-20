from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from testapp.forms import SignupForm


# Create your views here.
def home_page_view(request):
    return render(request,'home.html')

@login_required()
def java_exams_view(request):
    return render(request,'javaexams.html')

@login_required()
def python_exams_view(request):
    return render(request,"pythonexams.html")

@login_required()
def aptitude_exams_view(request):
    return render(request,"aptitudeexams.html")

def logout_view(request):
    return render(request,'logout.html')

def signup_view(request):
    form=SignupForm()
    if request.method=="POST":
        form=SignupForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'signup.html',{'form':form})

