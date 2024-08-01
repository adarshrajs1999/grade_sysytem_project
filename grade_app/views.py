from django.shortcuts import render,redirect
from grade_app.forms import User_register_form,Student_register_form,Teacher_register_form
from grade_app.models import User_model
from django.contrib.auth import authenticate,login,logout



# Create your views here.

def home(request):
    return render(request, 'home.html')

def register_dash(request):
    return render(request,'register_dash.html')

def user_dash(request):
    return render(request, 'user_dash.html')

def teacher_dash(request):
    return render(request,'teacher/teacher_dash.html')

def student_dash(request):
    return render(request,'student/student_dash.html')


def teacher_register(request):
    user_register_form_object = User_register_form()
    teacher_register_form_object = Teacher_register_form()
    if request.method == 'POST':
        user_register_form_object = User_register_form(request.POST)
        teacher_register_form_object = Teacher_register_form(request.POST)
        if user_register_form_object.is_valid() and teacher_register_form_object.is_valid():
            user_model_object = user_register_form_object.save(commit=False)
            user_model_object.is_teacher = True
            user_model_object.save()
            teacher_object = teacher_register_form_object.save(commit=False)
            teacher_object.user = user_model_object
            teacher_object.save()
            return redirect('/')
    return render(request,'teacher_register.html',{'user_register_form_object':user_register_form_object,'teacher_register_form_object':teacher_register_form_object})


def student_register(request):
    student_register_form_object = Student_register_form()
    user_register_form_object = User_register_form()
    if request.method == 'POST':
        student_register_form_object = Student_register_form(request.POST)
        user_register_form_object = User_register_form(request.POST)
        if user_register_form_object.is_valid() and student_register_form_object.is_valid():
            user_object = user_register_form_object.save(commit=False)
            user_object.is_student = True
            user_object.save()
            student_object = student_register_form_object.save(commit=False)
            student_object.user = user_object
            student_object.save()
            return redirect('/')
    return render(request, 'student_register.html',{'user_register_form_object':user_register_form_object,'student_register_form_object':student_register_form_object})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_object = authenticate(request,username=username,password=password)
        if user_object is not None:
            login(request,user_object)
            if user_object.is_teacher:
                return redirect('teacher_dash')
            elif user_object.is_student:
                return redirect('student_dash')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')