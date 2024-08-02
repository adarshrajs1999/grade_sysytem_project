from django.shortcuts import render,redirect
from .models import Student
from .forms import Student_update_form,Teacher_create_course_form,Teacher_create_grade_form

def teacher_view_student_details(request):
    student_objects = Student.objects.all()
    return render(request,'teacher/teacher_view_student_details.html',{'student_objects':student_objects})

def teacher_update_student_details(request,id):
    student_object = Student.objects.get(id = id)
    student_form_object = Student_update_form(instance=student_object)
    if request.method == 'POST':
        student_form_object = Student_update_form(request.POST,instance=student_object)
        student_form_object.save()
        return redirect('teacher_view_student_details')
    return render(request, 'teacher/teacher_update_student_details.html',{'student_form_object':student_form_object})

def teacher_delete_student_details(request, id):
    student_object = Student.objects.get(id=id)
    student_object.delete()
    return redirect('teacher_view_student_details')

def teacher_create_course(request):
    teacher_create_course_form_object = Teacher_create_course_form()
    if request.method == 'POST':
        teacher_create_course_form_object = Teacher_create_course_form(request.POST)
        if teacher_create_course_form_object.is_valid():
            teacher_create_course_form_object.save()
            return redirect('teacher_dash')
    return render(request,'teacher/teacher_create_course.html',{'teacher_create_course_form_object':teacher_create_course_form_object})

def teacher_create_grade(request):
    teacher_create_grade_form_object = Teacher_create_grade_form()
    if request.method == 'POST':
        teacher_create_grade_form_object = Teacher_create_grade_form(request.POST)
        if teacher_create_grade_form_object.is_valid():
            teacher_create_grade_form_object.save()
            return redirect('teacher_dash')
    return render(request,'teacher/teacher_create_grade.html',{'teacher_create_grade_form_object':teacher_create_grade_form_object})

