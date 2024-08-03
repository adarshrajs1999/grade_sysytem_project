from django.urls import path
from . import views,teacher_views,student_views

urlpatterns = [
    path('',views.home,name='home'),
    path('dash/', views.register_dash, name='register_dash'),
    path('user_dash/', views.user_dash, name='user_dash'),
    path('student_register/',views.student_register,name='student_register'),
    path('teacher_dash/',views.teacher_dash,name='teacher_dash'),
    path('student_dash/',views.student_dash,name='student_dash'),
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.logout_view,name='logout_view'),
    path('teacher_view_student_details/',teacher_views.teacher_view_student_details,name='teacher_view_student_details'),
    path('teacher_update_student_details/<int:id>/',teacher_views.teacher_update_student_details,name='teacher_update_student_details'),
    path('teacher_delete_student_details/<int:id>/',teacher_views.teacher_delete_student_details,name='teacher_delete_student_details'),
    path('teacher_create_course/',teacher_views.teacher_create_course,name='teacher_create_course'),
    path('teacher_view_courses/',teacher_views.teacher_view_courses,name='teacher_view_courses'),
    path('teacher_update_course/<int:id>/',teacher_views.teacher_update_course,name='teacher_update_course'),
    path('teacher_delete_course/<int:id>/',teacher_views.teacher_delete_course,name='teacher_delete_course'),
    path('teacher_create_grade/',teacher_views.teacher_create_grade,name='teacher_create_grade'),
    path('teacher_view_grades/',teacher_views.teacher_view_grades,name='teacher_view_grades'),
    path('teacher_update_grade/<int:id>/',teacher_views.teacher_update_grade,name='teacher_update_grade'),
    path('teacher_delete_grade/<int:id>/',teacher_views.teacher_delete_grade,name='teacher_delete_grade'),
    path('student_view_update_profile_details',student_views.student_view_update_profile_details,name='student_view_update_profile_details'),
    path('student_view_grades/',student_views.student_view_grades,name='student_view_grades'),
    path('student_calculate_gpa/',student_views.student_calculate_gpa,name='student_calculate_gpa')
    
        
]