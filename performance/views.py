from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.contrib.messages.views import SuccessMessageMixin
from .models import Pre_primary_performance, Lower_primary_performance, Upper_primary_performance
from school.models import Lower_primary


def lower_primary_html_to_pdf_view(request):
    
    context = {
        'object':Lower_primary_performance.objects.all().order_by('Student_name')
        }
    html_string = render_to_string('performance/lower_primary_performance_detail.html', context)

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
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
            student_name=self.object.student_name,
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
            student_name=self.object.student_name,
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

# lower primary views


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
