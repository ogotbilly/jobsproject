from django.urls import path
from attendance import views

urlpatterns = [
    path('home/attendance/pre-primary-1', views.pre_primary_1, name='pre-primary-1'),
    path('home/attendance/pre-primary-2', views.pre_primary_2, name='pre-primary-2'),
    path('home/attendance/grade-1', views.grade_1, name='grade-1'),
    path('home/attendance/grade-2', views.grade_2, name='grade-2'),
    path('home/attendance/grade-3', views.grade_3, name='grade-3'),
    path('home/attendance/grade-4', views.grade_4, name='grade-4'),
    path('home/attendance/grade-5', views.grade_5, name='grade-5'),
    path('home/attendance/grade-6', views.grade_6, name='grade-6'),


    



   
]
