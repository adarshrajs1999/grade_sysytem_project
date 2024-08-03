from django.shortcuts import render,redirect
from .models import Student,Grade
from .forms import Student_update_form

def student_view_update_profile_details(request):
    student_object = Student.objects.get(user = request.user)
    student_form_object = Student_update_form(instance=student_object)
    if request.method == 'POST':
        student_form_object = Student_update_form(request.POST,instance=student_object)
        student_form_object.save()
        return redirect('student_view_update_profile_details')
    return render(request, 'student/student_view_update_profile_details.html',{'student_form_object':student_form_object})

def student_view_grades(request):
    grade_objects = Grade.objects.filter(student__user = request.user)
    return render(request,'student/student_view_grades.html',{'grade_objects':grade_objects})