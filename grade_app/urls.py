from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('dash/', views.register_dash, name='register_dash'),
    path('user_dash/', views.user_dash, name='user_dash'),
    path('teacher_register/',views.teacher_register,name='teacher_register'),
    path('student_register/',views.student_register,name='student_register')
    
    

    
]