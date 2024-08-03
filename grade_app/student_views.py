from django.shortcuts import render,redirect
from .models import Student,Grade
from .forms import Student_profile_update_form

def student_view_update_profile_details(request):
    student_object = Student.objects.get(user = request.user)
    student_prfile_update_form_object = Student_profile_update_form(instance=student_object)
    if request.method == 'POST':
        student_prfile_update_form_object = Student_profile_update_form(request.POST,instance=student_object)
        student_prfile_update_form_object.save()
        return redirect('student_view_update_profile_details')
    return render(request, 'student/student_view_update_profile_details.html',{'student_prfile_update_form_object':student_prfile_update_form_object})

def student_view_grades(request):
    grade_objects = Grade.objects.filter(student__user = request.user)
    return render(request,'student/student_view_grades.html',{'grade_objects':grade_objects})

def student_calculate_gpa(request):
    grade_credicts_dictionary = {'a':4,'b':3,'c':2,'d':1,'e':0}
    grade_objects = Grade.objects.filter(student__user = request.user)
    grades_tuple = ((i.grade).lower() for i in grade_objects if (i.grade.lower()) in grade_credicts_dictionary)
    credits_tuple = (grade_credicts_dictionary[i] for i in grades_tuple)
    credits_sum =sum(credits_tuple)
    gpa = credits_sum*4
    return render(request,'student/student_calculate_gpa.html',{'gpa':gpa})