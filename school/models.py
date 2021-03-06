from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


# pre_primary model

class Pre_primary(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    PRE_PRIMARY_CLASS = (
        
        ('Two', 'Pre_primary 1'),
    )
    name_regex = RegexValidator(regex=r"^[a-zA-Z\s]+$", message="Only characters are allowed for Student name.")
    phone_number_regex = RegexValidator(regex=r'(\+254)\s*?(\d{3})\s*?(\d{3})\s*?(\d{3})', message="invalid phone number, phone number should be in the format of +254")
    reg_regex = RegexValidator(regex=r'[P]\d{4}', message="Registration number should start with 'P' followed by 4 digits for pre primary otherwise invalid registration number.")
    student_name = models.CharField(validators=[name_regex], max_length=100)
    registration_number = models.CharField(validators=[reg_regex], max_length=50)
    student_class = models.CharField(max_length=15, choices=PRE_PRIMARY_CLASS)
    student_gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    parent_name = models.CharField(max_length=100, blank=True)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, blank=True) # validators should be a list
    # date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse("student-details", kwargs={"pk": self.pk})

# lower primary model
class Pre_primary_2(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    PRE_PRIMARY_CLASS = (
        ('Two', 'Pre_primary 2'),
    )
    name_regex = RegexValidator(regex=r"^[a-zA-Z\s]+$", message="Only characters are allowed for Student name.")
    phone_number_regex = RegexValidator(regex=r'(\+254)\s*?(\d{3})\s*?(\d{3})\s*?(\d{3})', message="invalid phone number, phone number should be in the format of +254")
    reg_regex = RegexValidator(regex=r'[P]\d{4}', message="Registration number should start with 'P' followed by 4 digits for pre primary otherwise invalid registration number.")
    student_name = models.CharField(validators=[name_regex], max_length=100)
    registration_number = models.CharField(validators=[reg_regex], max_length=50)
    student_class = models.CharField(max_length=15, choices=PRE_PRIMARY_CLASS)
    student_gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    parent_name = models.CharField(max_length=100, blank=True)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, blank=True) # validators should be a list
    # date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse("pri-primary-two-details", kwargs={"pk": self.pk})

# lower primary model


class Lower_primary(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    LOWER_PRIMARY_CLASS = (
        
        ('Grade 1', 'Grade 1'),
    )
    name_regex = RegexValidator(regex=r"^[a-zA-Z\s]+$", message="Only characters are allowed for Student name.")
    phone_number_regex = RegexValidator(regex=r'(\+254)\s*?(\d{3})\s*?(\d{3})\s*?(\d{3})', message="invalid phone number, phone number should be in the format of +254")
    reg_regex = RegexValidator(regex=r'[L]\d{4}', message="Registration number should start with 'L' followed by 4 digits for lower primary otherwise invalid registration number.")
    student_name = models.CharField(validators=[name_regex], max_length=100)
    registration_number = models.CharField(validators=[reg_regex ], max_length=50)
    student_class = models.CharField(max_length=15, choices=LOWER_PRIMARY_CLASS)
    student_gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    parent_name = models.CharField(max_length=100)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{10,12}$', message="Phone number is invalid")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, blank=True) # validators should be a list
    #date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse("lower-primary-student-details", kwargs={"pk": self.pk})

class Lower_primary_grade_2(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    LOWER_PRIMARY_CLASS = (
      
        ('Grade 2', 'Grade 2'),
        
    )
    name_regex = RegexValidator(regex=r"^[a-zA-Z\s]+$", message="Only characters are allowed for Student name.")
    phone_number_regex = RegexValidator(regex=r'(\+254)\s*?(\d{3})\s*?(\d{3})\s*?(\d{3})', message="invalid phone number, phone number should be in the format of +254")
    reg_regex = RegexValidator(regex=r'[L]\d{4}', message="Registration number should start with 'L' followed by 4 digits for lower primary otherwise invalid registration number.")
    student_name = models.CharField(validators=[name_regex], max_length=100)
    registration_number = models.CharField(validators=[reg_regex ], max_length=50)
    student_class = models.CharField(max_length=15, choices=LOWER_PRIMARY_CLASS)
    student_gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    parent_name = models.CharField(max_length=100)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{10,12}$', message="Phone number is invalid")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, blank=True) # validators should be a list
    #date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse("lower-primary-grade-two-details", kwargs={"pk": self.pk})


class Lower_primary_grade_3(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    LOWER_PRIMARY_CLASS = (
        ('Grade 3', 'Grade 3'),
        
    )
    name_regex = RegexValidator(regex=r"^[a-zA-Z\s]+$", message="Only characters are allowed for Student name.")
    phone_number_regex = RegexValidator(regex=r'(\+254)\s*?(\d{3})\s*?(\d{3})\s*?(\d{3})', message="invalid phone number, phone number should be in the format of +254")
    reg_regex = RegexValidator(regex=r'[L]\d{4}', message="Registration number should start with 'L' followed by 4 digits for lower primary otherwise invalid registration number.")
    student_name = models.CharField(validators=[name_regex], max_length=100)
    registration_number = models.CharField(validators=[reg_regex ], max_length=50)
    student_class = models.CharField(max_length=15, choices=LOWER_PRIMARY_CLASS)
    student_gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    parent_name = models.CharField(max_length=100)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{10,12}$', message="Phone number is invalid")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, blank=True) # validators should be a list
    #date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse("lower-primary-grade-three-details", kwargs={"pk": self.pk})




class Upper_primary(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    UPPER_PRIMARY_CLASS = (
        
        ('Grade 4', 'Grade 4'),
    )
    name_regex = RegexValidator(regex=r"^[a-zA-Z\s]+$", message="Only characters are allowed for Student name.")
    phone_number_regex = RegexValidator(regex=r'(\+254)\s*?(\d{3})\s*?(\d{3})\s*?(\d{3})', message="invalid phone number, phone number should be in the format of +254")
    reg_regex = RegexValidator(regex=r'[U]\d{4}', message="Registration number should start with 'U' followed by 4 digits for upper primary otherwise invalid registration number.")
    student_name = models.CharField(validators=[name_regex], max_length=100)
    registration_number = models.CharField(validators=[reg_regex], max_length=50)
    student_class = models.CharField(max_length=15, choices=UPPER_PRIMARY_CLASS)
    student_gender = models.CharField(max_length=115, null=True, choices=GENDER_CHOICES)
    parent_name = models.CharField(max_length=100)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, blank=True) # validators should be a list
    #date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse("upper-primary-student-details", kwargs={"pk": self.pk})

class Upper_primary_grade_5(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    UPPER_PRIMARY_CLASS = (
        
        ('Grade 5', 'Grade 5'),
       
    )
    name_regex = RegexValidator(regex=r"^[a-zA-Z\s]+$", message="Only characters are allowed for Student name.")
    phone_number_regex = RegexValidator(regex=r'(\+254)\s*?(\d{3})\s*?(\d{3})\s*?(\d{3})', message="invalid phone number, phone number should be in the format of +254")
    reg_regex = RegexValidator(regex=r'[U]\d{4}', message="Registration number should start with 'U' followed by 4 digits for upper primary otherwise invalid registration number.")
    student_name = models.CharField(validators=[name_regex], max_length=100)
    registration_number = models.CharField(validators=[reg_regex], max_length=50)
    student_class = models.CharField(max_length=15, choices=UPPER_PRIMARY_CLASS)
    student_gender = models.CharField(max_length=115, null=True, choices=GENDER_CHOICES)
    parent_name = models.CharField(max_length=100)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, blank=True) # validators should be a list
    #date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse("upper-primary-grade-five-details", kwargs={"pk": self.pk})


class Upper_primary_grade_6(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    UPPER_PRIMARY_CLASS = (
        ('Grade 6', 'Grade 6'),
        
    )
    name_regex = RegexValidator(regex=r"^[a-zA-Z\s]+$", message="Only characters are allowed for Student name.")
    phone_number_regex = RegexValidator(regex=r'(\+254)\s*?(\d{3})\s*?(\d{3})\s*?(\d{3})', message="invalid phone number, phone number should be in the format of +254")
    reg_regex = RegexValidator(regex=r'[U]\d{4}', message="Registration number should start with 'U' followed by 4 digits for upper primary otherwise invalid registration number.")
    student_name = models.CharField(validators=[name_regex], max_length=100)
    registration_number = models.CharField(validators=[reg_regex], max_length=50)
    student_class = models.CharField(max_length=15, choices=UPPER_PRIMARY_CLASS)
    student_gender = models.CharField(max_length=115, null=True, choices=GENDER_CHOICES)
    parent_name = models.CharField(max_length=100)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, blank=True) # validators should be a list
    #date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse("upper-primary-grade-six-details", kwargs={"pk": self.pk})








    



