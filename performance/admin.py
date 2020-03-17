from django.contrib import admin
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


class SearchPrePrimary(admin.ModelAdmin):
    search_fields = ['Student_name']

    class Meta:
        model = Pre_primary_performance


class SearchLowerPrimary(admin.ModelAdmin):
    search_fields = ['Student_name']

    class Meta:
        model = Lower_primary_performance


class SearchUpperPrimary(admin.ModelAdmin):
    search_fields = ['Student_name']

    class Meta:
        model = Upper_primary_performance


admin.site.site_header = 'New Curriculum support System Admin Dashboard'
admin.site.register(Pre_primary_performance, SearchPrePrimary)
admin.site.register(Lower_primary_performance, SearchLowerPrimary)
admin.site.register(Upper_primary_performance, SearchUpperPrimary)
admin.site.register(Pre_primary_performance_2)
admin.site.register(Lower_primary_performance_grade_2)
admin.site.register(Lower_primary_performance_grade_3)
admin.site.register(Upper_primary_performance_grade_5)
admin.site.register(Upper_primary_performance_grade_6)

