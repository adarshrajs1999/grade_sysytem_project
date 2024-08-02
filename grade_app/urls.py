from django.urls import path
from . import views,teacher_views

urlpatterns = [
    path('',views.home,name='home'),
    path('dash/', views.register_dash, name='register_dash'),
    path('user_dash/', views.user_dash, name='user_dash'),
    path('teacher_register/',views.teacher_register,name='teacher_register'),
    path('student_register/',views.student_register,name='student_register'),
    path('teacher_dash/',views.teacher_dash,name='teacher_dash'),
    path('student_dash/',views.student_dash,name='student_dash'),
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.logout_view,name='logout_view'),
    path('teacher_view_student_details/',teacher_views.teacher_view_student_details,name='teacher_view_student_details'),
    path('teacher_update_student_details/<int:id>/',teacher_views.teacher_update_student_details,name='teacher_update_student_details'),
    path('teacher_delete_student_details/<int:id>/',teacher_views.teacher_delete_student_details,name='teacher_delete_student_details'),
    path('teacher_create_course/',teacher_views.teacher_create_course,name='teacher_create_course')
    
    

    
]