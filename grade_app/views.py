from django.shortcuts import render,redirect
from grade_app.forms import User_register_form



# Create your views here.

def home(request):
    return render(request, 'home.html')

def register_dash(request):
    return render(request,'register_dash.html')

def user_dash(request):
    return render(request, 'user_dash.html')


def teacher_register(request):
    user_register_form_object = User_register_form()
    if request.method == 'POST':
        user_register_form_object = User_register_form(request.POST)
        if user_register_form_object.is_valid():
            User_model_object = user_register_form_object.save(commit=False)
            user_register_form_object.is_teacher = True
            user_register_form_object.save()
            return redirect('/')
    return render(request,'teacher_register.html',{'user_register_form_object':user_register_form_object})




