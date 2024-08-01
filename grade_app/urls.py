from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('dash/', views.register_dash, name='register_dash'),
    path('user_dash/', views.user_dash, name='user_dash'),
    path('teacher_register/',views.teacher_register,name='teacher_register'),
    path('student_register/',views.student_register,name='student_register'),
    path('teacher_dash/',views.teacher_dash,name='teacher_dash'),
    path('student_dash/',views.student_dash,name='student_dash'),
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.logout_view,name='logout_view')
    
    

    
]