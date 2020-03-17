from django.contrib import admin
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


class SearchPrePrimary(admin.ModelAdmin):
    search_fields = [" student_name"]

    class Meta:
        model = Pre_primary


class SearchLowerPrimary(admin.ModelAdmin):
    search_fields = [" student_name"]

    class Meta:
        model = Lower_primary


class SearchUpperPrimary(admin.ModelAdmin):
    search_fields = [" student_name"]

    class Meta:
        model = Upper_primary


admin.site.register(Pre_primary, SearchPrePrimary)
admin.site.register(Lower_primary, SearchLowerPrimary)
admin.site.register(Upper_primary, SearchUpperPrimary)
admin.site.register(Pre_primary_2)
admin.site.register(Lower_primary_grade_2)
admin.site.register(Lower_primary_grade_3)
admin.site.register( Upper_primary_grade_5)
admin.site.register(Upper_primary_grade_6)

