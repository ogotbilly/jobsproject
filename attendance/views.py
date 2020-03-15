from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .models import Pre_primary_1_attendance, Lower_primary_attendance, Upper_primary_attendance
from .forms import PrePrimaryOneAttendanceForm, LowerPrimaryOneAttendanceForm, UpperPrimaryOneAttendanceForm

def pre_primary_1(request):
    context = {
        "students": Pre_primary_1_attendance.objects.all(),
    }

    return render(request, 'attendance/pre_primary_one.html', context)


# detail view for pre primary one 

def pre_primary_1_detail(request, id):

    today = datetime.now().strftime("%B %d, %Y")
    get_id = get_object_or_404(Pre_primary_1_attendance, pk=id)
    
    if request.method == 'POST':
        form = PrePrimaryOneAttendanceForm(request.POST)
    else:
        form = PrePrimaryOneAttendanceForm()

    context = {
        "get_id": get_id,
        "today": today,
        "form": form
    }

    return render(request, 'attendance/pre_primary_one_detail.html', context)


def pre_primary_2(request):
    context = {
        "students": Pre_primary_1_attendance.objects.all(),
    }

    return render(request, 'attendance/pre_primary_two.html', context)


def pre_primary_2_detail(request, id):

    today = datetime.now().strftime("%B %d, %Y")
    get_id = get_object_or_404(Pre_primary_1_attendance, pk=id)

    if request.method == 'POST':
        form = PrePrimaryOneAttendanceForm(request.POST)
    else:
        form = PrePrimaryOneAttendanceForm()

    context = {
        "get_id": get_id,
        "today": today, 
        "form": form
    }

    return render(request, 'attendance/pre_primary_two_detail.html', context)




def grade_1(request):
    context = {
        "students": Lower_primary_attendance.objects.all(),
    }

    return render(request, 'attendance/grade_one.html', context)

def grade_one_detail(request, id):

    today = datetime.now().strftime("%B %d, %Y")
    get_id = get_object_or_404(Pre_primary_1_attendance, pk=id)

    if request.method == 'POST':
        form = LowerPrimaryOneAttendanceForm(request.POST)
    else:
        form = LowerPrimaryOneAttendanceForm()

    context = {
        "get_id": get_id,
        "today": today, 
        "form": form
    }

    return render(request, 'attendance/grade_one_detail.html', context)




def grade_2(request):
    context = {
        "students": Lower_primary_attendance.objects.all(),
    }

    return render(request, 'attendance/grade_two.html', context)

def grade_two_detail(request, id):

    today = datetime.now().strftime("%B %d, %Y")
    get_id = get_object_or_404(Pre_primary_1_attendance, pk=id)

    if request.method == 'POST':
        form = LowerPrimaryOneAttendanceForm(request.POST)
    else:
        form = LowerPrimaryOneAttendanceForm()

    context = {
        "get_id": get_id,
        "today": today, 
        "form": form
    }

    return render(request, 'attendance/grade_two_detail.html', context)




def grade_3(request):
    context = {
        "students": Lower_primary_attendance.objects.all(),
    }

    return render(request, 'attendance/grade_three.html', context)


def grade_three_detail(request, id):

    today = datetime.now().strftime("%B %d, %Y")
    get_id = get_object_or_404(Pre_primary_1_attendance, pk=id)

    if request.method == 'POST':
        form = LowerPrimaryOneAttendanceForm(request.POST)
    else:
        form = LowerPrimaryOneAttendanceForm()

    context = {
        "get_id": get_id,
        "today": today, 
        "form": form
    }

    return render(request, 'attendance/grade_three_detail.html', context)

def grade_4(request):
    context = {
        "students": Upper_primary_attendance.objects.all(),
    }

    return render(request, 'attendance/grade_four.html', context)

def grade_four_detail(request, id):

    today = datetime.now().strftime("%B %d, %Y")
    get_id = get_object_or_404(Pre_primary_1_attendance, pk=id)

    if request.method == 'POST':
        form = UpperPrimaryOneAttendanceForm(request.POST)
    else:
        form = UpperPrimaryOneAttendanceForm()

    context = {
        "get_id": get_id,
        "today": today, 
        "form": form
    }

    return render(request, 'attendance/grade_four_detail.html', context)

def grade_5(request):
    context = {
        "students": Upper_primary_attendance.objects.all(),
    }

    return render(request, 'attendance/grade_five.html', context)

def grade_five_detail(request, id):

    today = datetime.now().strftime("%B %d, %Y")
    get_id = get_object_or_404(Pre_primary_1_attendance, pk=id)

    if request.method == 'POST':
        form = UpperPrimaryOneAttendanceForm(request.POST)
    else:
        form = UpperPrimaryOneAttendanceForm()

    context = {
        "get_id": get_id,
        "today": today, 
        "form": form
    }

    return render(request, 'attendance/grade_five_detail.html', context)

def grade_6(request):
    context = {
        "students": Upper_primary_attendance.objects.all(),
    }

    return render(request, 'attendance/grade_six.html', context)

def grade_six_detail(request, id):

    today = datetime.now().strftime("%B %d, %Y")
    get_id = get_object_or_404(Pre_primary_1_attendance, pk=id)

    if request.method == 'POST':
        form = UpperPrimaryOneAttendanceForm(request.POST)
    else:
        form = UpperPrimaryOneAttendanceForm()

    context = {
        "get_id": get_id,
        "today": today, 
        "form": form
    }

    return render(request, 'attendance/grade_six_detail.html', context)
