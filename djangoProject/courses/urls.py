from django.urls import path
from courses import views

app_name = 'courses'
urlpatterns = [
    path('courses/', views.course_list, name='courses'),
    path('<int:pk>/course/', views.course_detail, name='detail'),
    path('course_create/', views.course_create, name='course_create'),
    path('<int:pk>/course_edit/', views.course_edit, name='edit'),
    path('<int:pk>/delete/', views.course_delete, name='delete'),
    path('teacher_create/', views.teacher_create, name='teacher_create'),
    path('<int:pk>/teacher_edit/', views.teacher_edit, name='teacher_edit'),
    path('<int:pk>/teacher_delete/', views.teacher_delete, name='teacher_delete'),
    path('<int:pk>/teacher_detail',views.teacher_detail, name='teacher_detail')
]
