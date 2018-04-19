from django.shortcuts import render

from .models import EnrollmentItemByYear

# Create your views here.

def index(request):
  enrollment_list = EnrollmentItemByYear.objects.order_by('id')
  semester_list = list(EnrollmentItemByYear.objects.values_list('semester', flat=True).order_by('id'))
  number_list = list(EnrollmentItemByYear.objects.values_list('numberOfStudents', flat=True).order_by('id'))
  context = {'enrollment_list': enrollment_list, 
             'semester_list': semester_list,
             'number_list': number_list}
  return render(request, 'index.html', context=context)