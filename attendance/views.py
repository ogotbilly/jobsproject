from django.shortcuts import render
from .models import Pre_primary_1_attendance

def pre_primary_1(request):

    context = {
        "students": Pre_primary_1_attendance.objects.all()
    }

    return render(request, 'attendance/pre_primary_one.html', context)


def pre_primary_2(request):

    return render(request, 'attendance/pre_primary_two.html')


def grade_1(request):

    return render(request, 'attendance/grade_one.html')


def grade_2(request):

    return render(request, 'attendance/grade_two.html')


def grade_3(request):

    return render(request, 'attendance/grade_three.html')

def grade_4(request):

    return render(request, 'attendance/grade_four.html')

def grade_5(request):

    return render(request, 'attendance/grade_five.html')

def grade_6(request):

    return render(request, 'attendance/grade_six.html')
