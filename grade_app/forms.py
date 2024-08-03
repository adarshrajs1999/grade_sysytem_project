from django import forms
from django.contrib.auth.forms import UserCreationForm
from grade_app.models import User_model,Student,Course,Grade


class User_register_form(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput) 
    class Meta:
        model = User_model
        fields = ('username','password1','password2')


class Student_register_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('__all__')
        exclude = ('user','student_id')

class Student_update_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('__all__')
        exclude = ('user',)

class Teacher_create_course_form(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('__all__')

class Teacher_create_grade_form(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ('__all__')
        
class Course_update_form(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('__all__')





