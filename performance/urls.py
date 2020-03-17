from django.urls import path
from performance import views as performance_view


urlpatterns = [
   path('home/pre-primary-performance/', performance_view.PrePrimaryListView.as_view(), name="pre-primary-performance"),
   path('home/pre-primary-performance-create/', performance_view.PrePrimaryCreateView.as_view(), name="pre-primary-performance-create"),
   path('home/pre-primary-performance/<int:pk>/', performance_view.PrePrimaryDetailView.as_view(), name='pre-primary-performance-details'),
   path('home/pre-primary-performance/<int:pk>/print/', performance_view.pre_primary_html_to_pdf_view, name='pre-primary-performance-print'),
   path('home/pre-primary-performance/<int:pk>/update', performance_view.PrePrimaryUpdateView.as_view(), name='pre-primary-performance-update'),
   #lower primary two urls
   # path('home/pre-primary-performance/<int:pk>/print/', performance_view.pre_primary_html_to_pdf_view, name='pre-primary-performance-print'),
   path('home/pre-primary-two-performance/', performance_view.PrePrimaryTwoListView.as_view(), name="pre-primary-two-performance"),
   path('home/pre-primary-two-performance-create/', performance_view.PrePrimaryTwoCreateView.as_view(), name="pre-primary-two-performance-create"),
   path('home/pre-primary-two-performance/<int:pk>/', performance_view.PrePrimaryTwoDetailView.as_view(), name='pre-primary-two-performance-details'),
   path('home/pre-primary-two-performance/<int:pk>/update', performance_view.PrePrimaryTwoUpdateView.as_view(), name='pre-primary-two-performance-update'),
   #lower primary urls
   path('home/lower-primary-performance/', performance_view.LowerPrimaryListView.as_view(), name="lower-primary-performance"),
   path('home/lower-primary-performance-create/', performance_view.LowerPrimaryCreateView.as_view(), name="lower-primary-performance-create"),
   path('home/lower-primary-performance/<int:pk>/update/', performance_view.LowerPrimaryUpdateView.as_view(), name='lower-primary-performance-update'),
   path('home/lower-primary-performance/<int:pk>/print/', performance_view.lower_primary_html_to_pdf_view, name='lower-primary-performance-print'),
   path('home/lower-primary-performance/<int:pk>/', performance_view.LowerPrimaryDetailView.as_view(), name='lower-primary-performance-details'),
   #upper primary urls
   #lower primary grade two urls
   # path('home/lower-primary-performance/<int:pk>/print/', performance_view.lower_primary_html_to_pdf_view, name='lower-primary-performance-print'),
   path('home/lower-primary-grade-two-performance/', performance_view.LowerPrimaryGradeTwoListView.as_view(), name="lower-primary-grade-two-performance"),
   path('home/lower-primary-grade-two-performance-create/', performance_view.LowerPrimaryGradeTwoCreateView.as_view(), name="lower-primary-grade-two-performance-create"),
   path('home/lower-primary-grade-two-performance/<int:pk>/update/', performance_view.LowerPrimaryGradeTwoUpdateView.as_view(), name='lower-primary-grade-two-performance-update'),
   path('home/lower-primary-grade-two-performance/<int:pk>/', performance_view.LowerPrimaryGradeTwoDetailView.as_view(), name='lower-primary-grade-two-performance-details'),
   #upper primary urls
   #lower primary grade three urls
   # path('home/lower-primary-performance/<int:pk>/print/', performance_view.lower_primary_html_to_pdf_view, name='lower-primary-performance-print'),
   path('home/lower-primary-grade-three-performance/', performance_view.LowerPrimaryGradeThreeListView.as_view(), name="lower-primary-grade-three-performance"),
   path('home/lower-primary-grade-three-performance-create/', performance_view.LowerPrimaryGradeThreeCreateView.as_view(), name="lower-primary-grade-three-performance-create"),
   path('home/lower-primary-grade-three-performance/<int:pk>/update/', performance_view.LowerPrimaryGradeTheeUpdateView.as_view(), name='lower-primary-grade-three-performance-update'),
   path('home/lower-primary-grade-three-performance/<int:pk>/', performance_view.LowerPrimaryGradeThreeDetailView.as_view(), name='lower-primary-grade-three-performance-details'),
   #upper primary urls
   path('home/upper-primary-performance/', performance_view.UpperPrimaryListView.as_view(), name="upper-primary-performance"),
   path('home/upper-primary-performance-create/', performance_view.UpperPrimaryCreateView.as_view(), name="upper-primary-performance-create"),
   path('home/upper-primary-performance/<int:pk>/print/', performance_view.upper_primary_html_to_pdf_view, name='upper-primary-performance-print'),
   path('home/upper-primary-performance/<int:pk>/update/', performance_view.UpperPrimaryUpdateView.as_view(), name='upper-primary-performance-update'),
   path('home/upper-primary-performance/<int:pk>/', performance_view.UpperPrimaryDetailView.as_view(), name='upper-primary-performance-details'),
   #upper primary grade five urls
   # path('home/upper-primary-performance/<int:pk>/print/', performance_view.upper_primary_html_to_pdf_view, name='upper-primary-performance-print'),
   path('home/upper-primary-grade-five-performance/', performance_view.UpperPrimaryGradeFiveListView.as_view(), name="upper-primary-grade-five-performance"),
   path('home/upper-primary-grade-five-performance-create/', performance_view.UpperPrimaryGradeFiveCreateView.as_view(), name="upper-primary-grade-five-performance-create"),
   path('home/upper-primary-grade-five-performance/<int:pk>/update/', performance_view.UpperPrimaryGradeFiveUpdateView.as_view(), name='upper-primary-grade-five-performance-update'),
   path('home/upper-primary-grade-five-performance/<int:pk>/', performance_view.UpperPrimaryGradeFiveDetailView.as_view(), name='upper-primary-grade-five-performance-details'),
   #upper primary grade six urls
   # path('home/upper-primary-performance/<int:pk>/print/', performance_view.upper_primary_html_to_pdf_view, name='upper-primary-performance-print'),
   path('home/upper-primary-grade-six-performance/', performance_view.UpperPrimaryGradeSixListView.as_view(), name="upper-primary-grade-six-performance"),
   path('home/upper-primary-grade-six-performance-create/', performance_view.UpperPrimaryGradeSixCreateView.as_view(), name="upper-primary-grade-six-performance-create"),
   path('home/upper-primary-grade-six-performance/<int:pk>/update/', performance_view.UpperPrimaryGradeSixUpdateView.as_view(), name='upper-primary-grade-six-performance-update'),
   path('home/upper-primary-grade-six-performance/<int:pk>/', performance_view.UpperPrimaryGradeSixDetailView.as_view(), name='upper-primary-grade-six-performance-details'),
]
