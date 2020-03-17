from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.contrib.messages.views import SuccessMessageMixin
from school.models import Lower_primary
from .models import (
     Pre_primary_performance, 
     Lower_primary_performance,
     Upper_primary_performance, 
     Pre_primary_performance_2, 
     Lower_primary_performance_grade_2,
     Lower_primary_performance_grade_3,
     Upper_primary_performance_grade_5, 
     Upper_primary_performance_grade_6
     )


def lower_primary_html_to_pdf_view(request, pk):
    
    context = {
        'lower_primary':Lower_primary_performance.objects.all()
        }
    html_string = render_to_string('performance/lower_primary_performance_render_to_pdf.html', context)

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/student_performance.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('student_performance.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="student_performance.pdf"'
        return response

    return response

def pre_primary_html_to_pdf_view(request, pk):
    
    context = {
        'pre_primary':Pre_primary_performance.objects.all()
        }
    html_string = render_to_string('performance/pre_primary_performance_render_to_pdf.html', context)

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/student_performance.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('student_performance.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="student_performance.pdf"'
        return response

    return response

def upper_primary_html_to_pdf_view(request, pk):
    
    context = {
        'upper_primary':Pre_primary_performance.objects.all()
        }
    html_string = render_to_string('performance/upper_primary_performance_render_to_pdf.html', context)

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/student_performance.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('student_performance.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="student_performance.pdf"'
        return response

    return response


class PrePrimaryListView(ListView):
    model = Pre_primary_performance
    context_object_name = 'students'


class PrePrimaryCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Pre_primary_performance
    fields = '__all__'
    success_url = '/home/pre-primary-performance'
    success_message = "%(student_name)s results has been added successfully, to update if needed"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )


    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)


class PrePrimaryUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pre_primary_performance
    fields = ['Language_activities', 'Mathematical_activities', 'Environmental_activities', 'Psychomotor_and_creative_activities', 'Religious_education_activities', 'Teachers_comment']
    success_message = "%(student_name)s results has been added successfully updated"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class PrePrimaryDetailView(DetailView):
    model = Pre_primary_performance

# end of prepirimary one performance view

class PrePrimaryTwoListView(ListView):
    model = Pre_primary_performance_2
    context_object_name = 'students'


class PrePrimaryTwoCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Pre_primary_performance_2
    fields = '__all__'
    success_url = '/home/pre-primary-two-performance'
    success_message = "%(student_name)s results has been added successfully, to update if needed"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )


    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)


class PrePrimaryTwoUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pre_primary_performance_2
    fields = ['Language_activities', 'Mathematical_activities', 'Environmental_activities', 'Psychomotor_and_creative_activities', 'Religious_education_activities', 'Teachers_comment']
    success_message = "%(student_name)s results has been added successfully updated"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class PrePrimaryTwoDetailView(DetailView):
    model = Pre_primary_performance_2

# end of priprimary two performance view


class LowerPrimaryListView(ListView):
    model = Lower_primary_performance
    context_object_name = 'students'


class LowerPrimaryCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Lower_primary_performance
    fields = '__all__'
    success_url = '/home/lower-primary-performance'
    success_message = "%(student_name)s results has been added successfully, to update if needed"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)


class LowerPrimaryUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lower_primary_performance
    fields = ['English_language_activities', 'Literacy_activities', 'Kiswahili_language_activities', 'Mathematical_activities', 'Hygiene_and_nutrition_activities', 'Environmental_activities', 'Indigenous_language_activities', 'Movement_and_creative_activities', 'Religious_education_activities', 'Teachers_comment']
    success_message = "%(student_name)s results has been added successfully updated"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class LowerPrimaryDetailView(DetailView):
    model = Lower_primary_performance

# end of lower primary grade one performance view
# startof lower primary grade two performance view


class LowerPrimaryGradeTwoListView(ListView):
    model = Lower_primary_performance_grade_2
    context_object_name = 'students'


class LowerPrimaryGradeTwoCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Lower_primary_performance_grade_2
    fields = '__all__'
    success_url = '/home/lower-primary-grade-two-performance'
    success_message = "%(student_name)s results has been added successfully, to update if needed"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)


class LowerPrimaryGradeTwoUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lower_primary_performance_grade_2
    fields = ['English_language_activities', 'Literacy_activities', 'Kiswahili_language_activities', 'Mathematical_activities', 'Hygiene_and_nutrition_activities', 'Environmental_activities', 'Indigenous_language_activities', 'Movement_and_creative_activities', 'Religious_education_activities', 'Teachers_comment']
    success_message = "%(student_name)s results has been added successfully updated"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class LowerPrimaryGradeTwoDetailView(DetailView):
    model = Lower_primary_performance_grade_2


# end of lower primary grade two performance view
# startof lower primary grade three performance view


class LowerPrimaryGradeThreeListView(ListView):
    model = Lower_primary_performance_grade_3
    context_object_name = 'students'


class LowerPrimaryGradeThreeCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Lower_primary_performance_grade_3
    fields = '__all__'
    success_url = '/home/lower-primary-grade-three-performance'
    success_message = "%(student_name)s results has been added successfully, to update if needed"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)


class LowerPrimaryGradeTheeUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lower_primary_performance_grade_3
    fields = ['English_language_activities', 'Literacy_activities', 'Kiswahili_language_activities', 'Mathematical_activities', 'Hygiene_and_nutrition_activities', 'Environmental_activities', 'Indigenous_language_activities', 'Movement_and_creative_activities', 'Religious_education_activities', 'Teachers_comment']
    success_message = "%(student_name)s results has been added successfully updated"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class LowerPrimaryGradeThreeDetailView(DetailView):
    model = Lower_primary_performance_grade_3



# upper primary performance view


class UpperPrimaryListView(ListView):
    model = Upper_primary_performance
    context_object_name = 'students'


class UpperPrimaryCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Upper_primary_performance
    fields = '__all__'
    success_url = '/home/upper-primary-performance'
    success_message = "%(student_name)s results has been added successfully, to update if needed"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)


class UpperPrimaryUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Upper_primary_performance
    fields = ['English', 'Kiswahili_or_Kenya_Sign_Language', 'Home_Science', 'Mathematical', 'Agriculture', 'Science_and_Technology', 'Creative_Arts', 'Physical_and_Health_Education', 'Religious_education_activities', 'Social_Studies', 'Teachers_comment']
    success_message = "%(student_name)s results has been added successfully updated"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class UpperPrimaryDetailView(DetailView):
    model = Upper_primary_performance

# upper primary performance view


class UpperPrimaryGradeFiveListView(ListView):
    model = Upper_primary_performance_grade_5
    context_object_name = 'students'


class UpperPrimaryGradeFiveCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Upper_primary_performance_grade_5
    fields = '__all__'
    success_url = '/home/upper-primary-grade-five-performance'
    success_message = "%(student_name)s results has been added successfully, to update if needed"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)


class UpperPrimaryGradeFiveUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Upper_primary_performance_grade_5
    fields = ['English', 'Kiswahili_or_Kenya_Sign_Language', 'Home_Science', 'Mathematical', 'Agriculture', 'Science_and_Technology', 'Creative_Arts', 'Physical_and_Health_Education', 'Religious_education_activities', 'Social_Studies', 'Teachers_comment']
    success_message = "%(student_name)s results has been added successfully updated"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class UpperPrimaryGradeFiveDetailView(DetailView):
    model = Upper_primary_performance_grade_5
# end of upper primary grade 5

# upper primary perormance grade 6


class UpperPrimaryGradeSixListView(ListView):
    model = Upper_primary_performance_grade_6
    context_object_name = 'students'


class UpperPrimaryGradeSixCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Upper_primary_performance_grade_6
    fields = '__all__'
    success_url = '/home/upper-primary-grade-six-performance'
    success_message = "%(student_name)s results has been added successfully, to update if needed"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)


class UpperPrimaryGradeSixUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Upper_primary_performance_grade_6
    fields = ['English', 'Kiswahili_or_Kenya_Sign_Language', 'Home_Science', 'Mathematical', 'Agriculture', 'Science_and_Technology', 'Creative_Arts', 'Physical_and_Health_Education', 'Religious_education_activities', 'Social_Studies', 'Teachers_comment']
    success_message = "%(student_name)s results has been added successfully updated"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            student_name=self.object.Student_name,
        )

    def form_valid(self, form):
        if self.request.user:
            return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user:
            return True
        return False


class UpperPrimaryGradeSixDetailView(DetailView):
    model = Upper_primary_performance_grade_6
# end of upper primary grade 6