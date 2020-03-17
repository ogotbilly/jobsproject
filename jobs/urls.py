from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from user import views as user_views
from school import views as school_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('school.urls')),
    path('', include('performance.urls')),
    path('', include('messaging.urls')),
    path('', include('attendance.urls')),
    path('register/', user_views.register, name='register'),
    path('home/', school_views.home, name='home'),
    path('home/profile/', user_views.profile, name='profile'),
    path('home/dashboard/', school_views.dashboard, name='dashboard'),
    path('home/dashboard/fess-status/', school_views.fees_status, name='fees_status'),
    path('home/dashboard/<message_id>/delete', school_views.delete_messages, name="delete-message"),
    #start of pre_primary urls
    path('home/export-excel/', school_views.export_pre_primary_xls, name='pre-primary-export-excel'),
    path('home/students/', school_views.StudentsListView.as_view(), name='students'),
    path('home/students/new/', school_views.StudentsCreateView.as_view(), name='student-create'),
    path('home/students/<int:pk>/', school_views.StudentsDetailView.as_view(), name='student-details'),
    path('home/students/<int:pk>/update', school_views.StudentsUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete', school_views.StudentsDeleteView.as_view(), name='student-delete'),
    #lower primary urls
    #start of pre_primary_2 urls
    path('home/export-excel/', school_views.export_pre_primary_xls, name='pre-primary-export-excel'),
    path('home/pri-primary-two/', school_views.StudentsListPrePrimaryTwoView.as_view(), name='pri-primary-two-list'),
    path('home/pri-primary-two/new/', school_views.StudentsPrePrimaryTwoCreateView.as_view(), name='pri-primary-two-create'),
    path('home/pri-primary-two/<int:pk>/', school_views.StudentsPrePrimaryTwoDetailView.as_view(), name='pri-primary-two-details'),
    path('home/pri-primary-two/<int:pk>/update', school_views.StudentsPrePrimaryTwoUpdateView.as_view(), name='pri-primary-two-update'),
    path('pri-primary-two/<int:pk>/delete', school_views.StudentsPrePrimaryTwoDeleteView.as_view(), name='pri-primary-two-delete'),
    #lower primary urls_2
    path('home/lower-primary-students/lower-primary-export-excel/', school_views.export_lower_primary_xls, name='lower-primary-export-excel'),
    path('home/lower-primary-students/', school_views.LowerPrimaryStudentsListView.as_view(), name='lower-primary-students'),
    path('home/lower-primary-students/<int:pk>/', school_views.LowerPrimaryStudentsDetailView.as_view(), name='lower-primary-student-details'),
    path('home/lower-primary-students/new/', school_views.LowerPrimaryStudentsCreateView.as_view(), name='lower-primary-student-create'),
    path('home/lower-primary-students/<int:pk>/update', school_views.LowerPrimaryStudentsUpdateView.as_view(), name='lower-primary-student-update'),
    path('lower-primary-students/<int:pk>/delete', school_views.LowerPrimaryStudentsDeleteView.as_view(), name='lower-primary-student-delete'),
    #end of lower primary grade two urls 
    path('home/lower-primary-students/lower-primary-export-excel/', school_views.export_lower_primary_xls, name='lower-primary-export-excel'),
    path('home/lower-primary-grade-two-list/', school_views.LowerPrimaryGradeTwoStudentsListView.as_view(), name='lower-primary-grade-two-list'),
    path('home/lower-primary-grade-two-list/<int:pk>/', school_views.LowerPrimaryGradeTwoStudentsDetailView.as_view(), name='lower-primary-grade-two-details'),
    path('home/lower-primary-grade-two-list/new/', school_views.LowerPrimaryGradeTwoStudentsCreateView.as_view(), name='lower-primary-grade-two-create'),
    path('home/lower-primary-grade-two-list/<int:pk>/update', school_views.LowerPrimaryGradeTwoStudentsUpdateView.as_view(), name='lower-primary-grade-two-update'),
    path('lower-primary-grade-two-list/<int:pk>/delete', school_views.LowerPrimaryGradeTwoStudentsDeleteView.as_view(), name='lower-primary-grade-two-delete'),
    #end of lower primary grade hree uls
     path('home/lower-primary-students/lower-primary-export-excel/', school_views.export_lower_primary_xls, name='lower-primary-export-excel'),
    path('home/lower-primary-grade-three-list/', school_views.LowerPrimaryGradeThreeStudentsListView.as_view(), name='lower-primary-grade-three-list'),
    path('home/lower-primary-grade-three-list/<int:pk>/', school_views.LowerPrimaryGradeThreeStudentsDetailView.as_view(), name='lower-primary-grade-three-details'),
    path('home/lower-primary-grade-three-list/new/', school_views.LowerPrimaryGradeThreeStudentsCreateView.as_view(), name='lower-primary-grade-three-create'),
    path('home/lower-primary-grade-three-list/<int:pk>/update', school_views.LowerPrimaryGradeThreeStudentsUpdateView.as_view(), name='lower-primary-grade-three-update'),
    path('lower-primary-grade-three-list/<int:pk>/delete', school_views.LowerPrimaryGradeThreeStudentsDeleteView.as_view(), name='lower-primary-grade-three-delete'),
    #end of lower primary grade three uls
    path('home/upper-primary-students/upper-primary-export-excel/', school_views.export_upper_primary_xls, name='upper-primary-export-excel'),
    path('home/upper-primary-students/', school_views.UpperPrimaryStudentsListView.as_view(), name='upper-primary-students'),
    path('home/upper-primary-students/<int:pk>/', school_views.UpperPrimaryStudentsDetailView.as_view(), name='upper-primary-student-details'),
    path('home/upper-primary-students/new/', school_views.UpperPrimaryStudentsCreateView.as_view(), name='upper-primary-student-create'),
    path('home/upper-primary-students/<int:pk>/update', school_views.UpperPrimaryStudentsUpdateView.as_view(), name='upper-primary-student-update'),
    path('upper-primary-students/<int:pk>/delete', school_views.UpperPrimaryStudentsDeleteView.as_view(), name='upper-primary-student-delete'),
    #end of upper primary grade five urls
    path('home/upper-primary-students/upper-primary-export-excel/', school_views.export_upper_primary_xls, name='upper-primary-export-excel'),
    path('home/upper-primary-grade-five/', school_views.UpperPrimaryGradeFiveStudentsListView.as_view(), name='upper-primary-grade-five-list'),
    path('home/upper-primary-grade-five/<int:pk>/', school_views.UpperPrimaryGradeFiveStudentsDetailView.as_view(), name='upper-primary-grade-five-details'),
    path('home/upper-primary-grade-five/new/', school_views.UpperPrimaryGradeFiveStudentsCreateView.as_view(), name='upper-primary-grade-five-create'),
    path('home/upper-primary-grade-five/<int:pk>/update', school_views.UpperPrimaryGradeFiveStudentsUpdateView.as_view(), name='upper-primary-grade-five-update'),
    path('upper-primary-grade-five/<int:pk>/delete', school_views.UpperPrimaryGradeFiveStudentsDeleteView.as_view(), name='upper-primary-grade-five-delete'),
    #end of upper primary urls
    path('home/upper-primary-students/upper-primary-export-excel/', school_views.export_upper_primary_xls, name='upper-primary-export-excel'),
    path('home/upper-primary-grade-six/', school_views.UpperPrimaryGradeSixStudentsListView.as_view(), name='upper-primary-grade-six-list'),
    path('home/upper-primary-grade-six/<int:pk>/', school_views.UpperPrimaryGradeSixStudentsDetailView.as_view(), name='upper-primary-grade-six-details'),
    path('home/upper-primary-grade-six/new/', school_views.UpperPrimaryGradeSixStudentsCreateView.as_view(), name='upper-primary-grade-six-create'),
    path('home/upper-primary-grade-six/<int:pk>/update', school_views.UpperPrimaryGradeSixStudentsUpdateView.as_view(), name='upper-primary-grade-six-update'),
    path('upper-primary-grade-six/<int:pk>/delete', school_views.UpperPrimaryGradeSixStudentsDeleteView.as_view(), name='upper-primary-grade-six-delete'),
    #end of upper primary urls
    path('home/track-progress/', school_views.track_progress, name='track-progress'),
    path('home/fees-status/', school_views.fees_status, name='fees-status'),
    path('home/change-password/', school_views.change_password, name='change-password'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
