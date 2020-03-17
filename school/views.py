from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import xlwt
from django.http import HttpResponse
from messaging.models import TwilioMesaage
from .models import (
                    Pre_primary, 
                    Lower_primary,
                    Upper_primary,
                    Pre_primary_2, 
                    Lower_primary_grade_2, 
                    Lower_primary_grade_3,
                    Upper_primary_grade_5, 
                    Upper_primary_grade_6
)




@login_required
def home(request):
    return render(request, 'school/home.html')


@login_required
def dashboard(request):
    context = {
        "message_sent": TwilioMesaage.objects.all()
    }
    
    return render(request, 'school/dashboard.html', context)

@login_required

def delete_messages(request, message_id):
    TwilioMesaage.objects.get(id=message_id).delete()
    messages.success(request, 'Message has been deleted successfully.')
    return redirect("dashboard")


def track_progress(request):
    return render(request, 'school/track_progress.html')


def fees_status(request):
    return render(request, 'school/fees_status.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('home')
        else:
            messages.error(request, 'There was an error, please try again latter')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'school/change_password.html', {"form": form})

# class based views for pre primary_one


class StudentsListView(ListView):
    model = Pre_primary
    template_name = 'school/addstudent.html'
    context_object_name = 'students'
   


class StudentsDetailView(DetailView):
    model = Pre_primary


class StudentsCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Pre_primary
    fields = '__all__'
    success_url = '/home/students/'
    success_message = "%(student_name)s has been registared successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)


class StudentsUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pre_primary
    fields = '__all__'
    success_message = "%(student_name)s has been updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )
    

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class StudentsDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pre_primary
    success_url = '/home/students/'
    success_message = "%(student_name)s results has been deleted successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )


    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False

# class based views for lower primary_two students

class StudentsListPrePrimaryTwoView(ListView):
    model = Pre_primary_2
    context_object_name = 'students'
   


class StudentsPrePrimaryTwoDetailView(DetailView):
    model = Pre_primary_2


class StudentsPrePrimaryTwoCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Pre_primary_2
    fields = '__all__'
    success_url = '/home/pri-primary-two-list/'
    success_message = "%(student_name)s has been registared successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)


class StudentsPrePrimaryTwoUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pre_primary_2
    fields = '__all__'
    success_message = "%(student_name)s has been updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )
    

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class StudentsPrePrimaryTwoDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pre_primary_2
    success_url = '/home/pri-primary-two-list/'
    success_message = "%(student_name)s results has been deleted successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )


    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False

# class based views for lower primary_2 students


class LowerPrimaryStudentsListView(ListView):
    model = Lower_primary
    template_name = 'school/lower_primary.html'
    context_object_name = 'students'


class LowerPrimaryStudentsDetailView(DetailView):
    model = Lower_primary


class LowerPrimaryStudentsCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Lower_primary
    fields = '__all__'
    success_url = '/home/lower-primary-students'
    success_message = "%(student_name)s has been registared successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)


class LowerPrimaryStudentsUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Lower_primary
    fields = '__all__'
    success_message = "%(student_name)s details has been updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class LowerPrimaryStudentsDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lower_primary
    success_url = '/home/lower-primary-students/'
    success_message = "%(student_name)s details has been deleted successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


# class based views for lower primary grade two

class LowerPrimaryGradeTwoStudentsListView(ListView):
    model = Lower_primary_grade_2
    context_object_name = 'students'


class LowerPrimaryGradeTwoStudentsDetailView(DetailView):
    model = Lower_primary_grade_2


class LowerPrimaryGradeTwoStudentsCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Lower_primary_grade_2
    fields = '__all__'
    success_url = '/home/lower-primary-grade-two-list/'
    success_message = "%(student_name)s has been registared successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)


class LowerPrimaryGradeTwoStudentsUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Lower_primary_grade_2
    fields = '__all__'
    success_message = "%(student_name)s details has been updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class LowerPrimaryGradeTwoStudentsDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lower_primary_grade_2
    success_url = '/home/lower-primary-grade-two-list/'
    success_message = "%(student_name)s details has been deleted successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


# class based views for upper primary
# class based views for lower primary grade three

class LowerPrimaryGradeThreeStudentsListView(ListView):
    model = Lower_primary_grade_3
    context_object_name = 'students'


class LowerPrimaryGradeThreeStudentsDetailView(DetailView):
    model = Lower_primary_grade_3


class LowerPrimaryGradeThreeStudentsCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Lower_primary_grade_3
    fields = '__all__'
    success_url = '/home/lower-primary-grade-three-list/'
    success_message = "%(student_name)s has been registared successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)


class LowerPrimaryGradeThreeStudentsUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Lower_primary_grade_3
    fields = '__all__'
    success_message = "%(student_name)s details has been updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class LowerPrimaryGradeThreeStudentsDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lower_primary_grade_3
    success_url = '/home/lower-primary-grade-three-list/'
    success_message = "%(student_name)s details has been deleted successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


# class based views for upper primary

class UpperPrimaryStudentsListView(ListView):
    model = Upper_primary
    context_object_name = 'students'


class UpperPrimaryStudentsDetailView(DetailView):
    model = Upper_primary


class UpperPrimaryStudentsCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Upper_primary
    fields = '__all__'
    success_url = '/home/upper-primary-students'
    success_message = "%(student_name)s has been registared successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )


    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)


class UpperPrimaryStudentsUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Upper_primary
    fields = '__all__'
    success_message = "%(student_name)s details has been updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class UpperPrimaryStudentsDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Upper_primary
    success_url = '/home/upper-primary-students/'
    success_message = "%(student_name)s details has been updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


# end of class based views for upper primary grade five
class UpperPrimaryGradeFiveStudentsListView(ListView):
    model = Upper_primary_grade_5
    context_object_name = 'students'


class UpperPrimaryGradeFiveStudentsDetailView(DetailView):
    model = Upper_primary_grade_5


class UpperPrimaryGradeFiveStudentsCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Upper_primary_grade_5
    fields = '__all__'
    success_url = '/home/upper-primary-grade-five/'
    success_message = "%(student_name)s has been registared successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )


    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)


class UpperPrimaryGradeFiveStudentsUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Upper_primary_grade_5
    fields = '__all__'
    success_message = "%(student_name)s details has been updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class UpperPrimaryGradeFiveStudentsDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Upper_primary_grade_5
    success_url = '/home/upper-primary-grade-five/'
    success_message = "%(student_name)s details has been updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


# end of class based views for upper primary
# end of class based views for upper primary grade six
class UpperPrimaryGradeSixStudentsListView(ListView):
    model = Upper_primary_grade_6
    context_object_name = 'students'


class UpperPrimaryGradeSixStudentsDetailView(DetailView):
    model = Upper_primary_grade_6


class UpperPrimaryGradeSixStudentsCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Upper_primary_grade_6
    fields = '__all__'
    success_url = '/home/upper-primary-grade-six/'
    success_message = "%(student_name)s has been registared successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )


    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)


class UpperPrimaryGradeSixStudentsUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Upper_primary_grade_6
    fields = '__all__'
    success_message = "%(student_name)s details has been updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class UpperPrimaryGradeSixStudentsDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Upper_primary_grade_6
    success_url = '/home/upper-primary-grade-six/'
    success_message = "%(student_name)s details has been updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.student_name,
        )

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


# end of class based views for upper primary

# export to excel pre primary
def export_pre_primary_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="pre_primary_students.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Pre_Primary Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id', 'Student_name', 'Registration_number ', 'Student_class', 'Student_gender', 'Parent_name', 'Phone_number', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Pre_primary.objects.all().values_list('id', 'student_name', 'registration_number', 'student_class', 'student_gender', 'parent_name', 'phone_number')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

# export to excel lower primary
def export_lower_primary_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="lower_primary_students.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('lower_Primary Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id', 'Student_name', 'Registration_number ', 'Student_class', 'Student_gender', 'Parent_name', 'Phone_number', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Lower_primary.objects.all().values_list('id', 'student_name', 'registration_number', 'student_class', 'student_gender', 'parent_name', 'phone_number')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

# export to excel upper primary
def export_upper_primary_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="upper_primary_students.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Upper_Primary Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id', 'Student_name', 'Registration_number ', 'Student_class', 'Student_gender', 'Parent_name', 'Phone_number', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Upper_primary.objects.all().values_list('id', 'student_name', 'registration_number', 'student_class', 'student_gender', 'parent_name', 'phone_number')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

# viewing all the messages sent



