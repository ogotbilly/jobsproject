from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from school.models import (
                    Pre_primary, 
                    Lower_primary,
                    Upper_primary,
                    Pre_primary_2, 
                    Lower_primary_grade_2, 
                    Lower_primary_grade_3,
                    Upper_primary_grade_5, 
                    Upper_primary_grade_6
)


class Pre_primary_performance(models.Model):
    valid = RegexValidator(regex=r'^[0-9]+$', message="only digits are required.")
    Student_name = models.OneToOneField(Pre_primary, on_delete=models.CASCADE)
    Language_activities = models.CharField(validators=[valid], max_length=255)
    Mathematical_activities = models.CharField(validators=[valid], max_length=255)
    Environmental_activities = models.CharField(validators=[valid], max_length=255)
    Psychomotor_and_creative_activities = models.CharField(validators=[valid], max_length=255)
    Religious_education_activities = models.CharField(validators=[valid], max_length=255)
    Teachers_comment = models.TextField()

    def __str__(self):
        return str(self.Student_name)

    def get_absolute_url(self):
        return reverse("pre-primary-performance-details", kwargs={"pk": self.pk})
    
    def get_total_pre_primary(self):
        return (
        int(self.Language_activities)
        + int(self.Mathematical_activities)
        + int(self.Environmental_activities) 
        + int(self.Psychomotor_and_creative_activities)
        + int(self.Religious_education_activities) 
        )

class Pre_primary_performance_2(models.Model):
    valid = RegexValidator(regex=r'^[0-9]+$', message="only digits are required.")
    Student_name = models.OneToOneField(Pre_primary_2, on_delete=models.CASCADE)
    Language_activities = models.CharField(validators=[valid], max_length=255)
    Mathematical_activities = models.CharField(validators=[valid], max_length=255)
    Environmental_activities = models.CharField(validators=[valid], max_length=255)
    Psychomotor_and_creative_activities = models.CharField(validators=[valid], max_length=255)
    Religious_education_activities = models.CharField(validators=[valid], max_length=255)
    Teachers_comment = models.TextField()

    def __str__(self):
        return str(self.Student_name)

    def get_absolute_url(self):
        return reverse("pre-primary-two-performance-details", kwargs={"pk": self.pk})
    
    def get_total_pre_primary(self):
        return (
        int(self.Language_activities)
        + int(self.Mathematical_activities)
        + int(self.Environmental_activities) 
        + int(self.Psychomotor_and_creative_activities)
        + int(self.Religious_education_activities) 
        )



class Lower_primary_performance(models.Model):
    valid = RegexValidator(regex=r'^[0-9]+$', message="only digits are required.")
    Student_name = models.OneToOneField(Lower_primary, on_delete=models.CASCADE)
    English_language_activities = models.CharField(validators=[valid], max_length=255)
    Literacy_activities = models.CharField(validators=[valid], max_length=255)
    Kiswahili_language_activities = models.CharField(validators=[valid], max_length=255)
    Mathematical_activities = models.CharField(validators=[valid], max_length=255)
    Hygiene_and_nutrition_activities = models.CharField(validators=[valid], max_length=255)
    Environmental_activities = models.CharField(validators=[valid], max_length=255)
    Indigenous_language_activities = models.CharField(validators=[valid], max_length=255)
    Movement_and_creative_activities = models.CharField(validators=[valid], max_length=255)
    Religious_education_activities = models.CharField(validators=[valid], max_length=255)
    Teachers_comment = models.TextField()

    def __str__(self):
        return str(self.Student_name)

    def get_absolute_url(self):
        return reverse("lower-primary-performance-details", kwargs={"pk": self.pk})
    
    def get_total(self):
        return (
        int(self.English_language_activities)
        + int(self.Literacy_activities )
        + int(self.Kiswahili_language_activities) 
        + int(self.Mathematical_activities)
        + int(self.Hygiene_and_nutrition_activities) 
        + int(self.Environmental_activities) 
        + int(self.Indigenous_language_activities) 
        + int(self.Movement_and_creative_activities) 
        + int(self.Religious_education_activities) 
        )
class Lower_primary_performance_grade_2(models.Model):
    valid = RegexValidator(regex=r'^[0-9]+$', message="only digits are required.")
    Student_name = models.OneToOneField(Lower_primary_grade_2, on_delete=models.CASCADE)
    English_language_activities = models.CharField(validators=[valid], max_length=255)
    Literacy_activities = models.CharField(validators=[valid], max_length=255)
    Kiswahili_language_activities = models.CharField(validators=[valid], max_length=255)
    Mathematical_activities = models.CharField(validators=[valid], max_length=255)
    Hygiene_and_nutrition_activities = models.CharField(validators=[valid], max_length=255)
    Environmental_activities = models.CharField(validators=[valid], max_length=255)
    Indigenous_language_activities = models.CharField(validators=[valid], max_length=255)
    Movement_and_creative_activities = models.CharField(validators=[valid], max_length=255)
    Religious_education_activities = models.CharField(validators=[valid], max_length=255)
    Teachers_comment = models.TextField()

    def __str__(self):
        return str(self.Student_name)

    def get_absolute_url(self):
        return reverse("lower-primary-grade-two-performance-details", kwargs={"pk": self.pk})
    
    def get_total(self):
        return (
        int(self.English_language_activities)
        + int(self.Literacy_activities )
        + int(self.Kiswahili_language_activities) 
        + int(self.Mathematical_activities)
        + int(self.Hygiene_and_nutrition_activities) 
        + int(self.Environmental_activities) 
        + int(self.Indigenous_language_activities) 
        + int(self.Movement_and_creative_activities) 
        + int(self.Religious_education_activities) 
        )

class Lower_primary_performance_grade_3(models.Model):
    valid = RegexValidator(regex=r'^[0-9]+$', message="only digits are required.")
    Student_name = models.OneToOneField(Lower_primary_grade_3, on_delete=models.CASCADE)
    English_language_activities = models.CharField(validators=[valid], max_length=255)
    Literacy_activities = models.CharField(validators=[valid], max_length=255)
    Kiswahili_language_activities = models.CharField(validators=[valid], max_length=255)
    Mathematical_activities = models.CharField(validators=[valid], max_length=255)
    Hygiene_and_nutrition_activities = models.CharField(validators=[valid], max_length=255)
    Environmental_activities = models.CharField(validators=[valid], max_length=255)
    Indigenous_language_activities = models.CharField(validators=[valid], max_length=255)
    Movement_and_creative_activities = models.CharField(validators=[valid], max_length=255)
    Religious_education_activities = models.CharField(validators=[valid], max_length=255)
    Teachers_comment = models.TextField()

    def __str__(self):
        return str(self.Student_name)

    def get_absolute_url(self):
        return reverse("lower-primary-grade-three-performance-details", kwargs={"pk": self.pk})
    
    def get_total(self):
        return (
        int(self.English_language_activities)
        + int(self.Literacy_activities )
        + int(self.Kiswahili_language_activities) 
        + int(self.Mathematical_activities)
        + int(self.Hygiene_and_nutrition_activities) 
        + int(self.Environmental_activities) 
        + int(self.Indigenous_language_activities) 
        + int(self.Movement_and_creative_activities) 
        + int(self.Religious_education_activities) 
        )




class Upper_primary_performance(models.Model):
    valid = RegexValidator(regex=r'^[0-9]+$', message="only digits are required.")
    Student_name = models.OneToOneField(Upper_primary, on_delete=models.CASCADE)
    English = models.CharField(validators=[valid], max_length=255)
    Kiswahili_or_Kenya_Sign_Language = models.CharField(validators=[valid], max_length=255)
    Home_Science = models.CharField(validators=[valid], max_length=255)
    Mathematical = models.CharField(validators=[valid], max_length=255)
    Agriculture = models.CharField(validators=[valid], max_length=255)
    Science_and_Technology = models.CharField(validators=[valid], max_length=255)
    Creative_Arts = models.CharField(validators=[valid], max_length=255)
    Physical_and_Health_Education = models.CharField(validators=[valid], max_length=255)
    Religious_education_activities = models.CharField(validators=[valid], max_length=255)
    Social_Studies = models.CharField(validators=[valid], max_length=255)
    Teachers_comment = models.TextField()

    def __str__(self):
        return str(self.Student_name)

    def get_absolute_url(self):
        return reverse("upper-primary-performance-details", kwargs={"pk": self.pk})


    def get_total_upper_primary(self):
        return (
        int(self.English)
        + int(self.Kiswahili_or_Kenya_Sign_Language)
        + int(self.Home_Science) 
        + int(self.Mathematical)
        + int(self.Agriculture) 
        + int(self.Science_and_Technology) 
        + int(self.Creative_Arts) 
        + int(self.Physical_and_Health_Education) 
        + int(self.Religious_education_activities) 
        + int(self.Social_Studies) 

        )

class Upper_primary_performance_grade_5(models.Model):
    valid = RegexValidator(regex=r'^[0-9]+$', message="only digits are required.")
    Student_name = models.OneToOneField(Upper_primary_grade_5, on_delete=models.CASCADE)
    English = models.CharField(validators=[valid], max_length=255)
    Kiswahili_or_Kenya_Sign_Language = models.CharField(validators=[valid], max_length=255)
    Home_Science = models.CharField(validators=[valid], max_length=255)
    Mathematical = models.CharField(validators=[valid], max_length=255)
    Agriculture = models.CharField(validators=[valid], max_length=255)
    Science_and_Technology = models.CharField(validators=[valid], max_length=255)
    Creative_Arts = models.CharField(validators=[valid], max_length=255)
    Physical_and_Health_Education = models.CharField(validators=[valid], max_length=255)
    Religious_education_activities = models.CharField(validators=[valid], max_length=255)
    Social_Studies = models.CharField(validators=[valid], max_length=255)
    Teachers_comment = models.TextField()

    def __str__(self):
        return str(self.Student_name)

    def get_absolute_url(self):
        return reverse("upper-primary-grade-five-performance-details", kwargs={"pk": self.pk})


    def get_total_upper_primary(self):
        return (
        int(self.English)
        + int(self.Kiswahili_or_Kenya_Sign_Language)
        + int(self.Home_Science) 
        + int(self.Mathematical)
        + int(self.Agriculture) 
        + int(self.Science_and_Technology) 
        + int(self.Creative_Arts) 
        + int(self.Physical_and_Health_Education) 
        + int(self.Religious_education_activities) 
        + int(self.Social_Studies) 

        )
class Upper_primary_performance_grade_6(models.Model):
    valid = RegexValidator(regex=r'^[0-9]+$', message="only digits are required.")
    Student_name = models.OneToOneField(Upper_primary_grade_6, on_delete=models.CASCADE)
    English = models.CharField(validators=[valid], max_length=255)
    Kiswahili_or_Kenya_Sign_Language = models.CharField(validators=[valid], max_length=255)
    Home_Science = models.CharField(validators=[valid], max_length=255)
    Mathematical = models.CharField(validators=[valid], max_length=255)
    Agriculture = models.CharField(validators=[valid], max_length=255)
    Science_and_Technology = models.CharField(validators=[valid], max_length=255)
    Creative_Arts = models.CharField(validators=[valid], max_length=255)
    Physical_and_Health_Education = models.CharField(validators=[valid], max_length=255)
    Religious_education_activities = models.CharField(validators=[valid], max_length=255)
    Social_Studies = models.CharField(validators=[valid], max_length=255)
    Teachers_comment = models.TextField()

    def __str__(self):
        return str(self.Student_name)

    def get_absolute_url(self):
        return reverse("upper-primary-grade-six-performance-details", kwargs={"pk": self.pk})


    def get_total_upper_primary(self):
        return (
        int(self.English)
        + int(self.Kiswahili_or_Kenya_Sign_Language)
        + int(self.Home_Science) 
        + int(self.Mathematical)
        + int(self.Agriculture) 
        + int(self.Science_and_Technology) 
        + int(self.Creative_Arts) 
        + int(self.Physical_and_Health_Education) 
        + int(self.Religious_education_activities) 
        + int(self.Social_Studies) 

        )
      



    





