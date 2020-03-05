from django.db import models
from django.utils import timezone
from school.models import Pre_primary, Lower_primary, Upper_primary

class Pre_primary_1_attendance(models.Model):

    student_class = models.ForeignKey(Pre_primary, on_delete=models.CASCADE)
    monday = models.BooleanField("Mondday", default=False)
    tuesday = models.BooleanField("Tuesday", default=False)
    wednessday = models.BooleanField("Wednessday", default=False)
    thursday = models.BooleanField("thursday", default=False)
    friday = models.BooleanField("Friday", default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.student_class)
    