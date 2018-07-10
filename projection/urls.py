from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projection/enrollment', views.enrollment_index, name='enrollment'),
    path('projection/attemptedCredits', views.enrollment_index, name='attemptedCredits'),
    path('projection/contactHours', views.enrollment_index, name='contactHours'),
]
