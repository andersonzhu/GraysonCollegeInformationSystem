from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import ProjectionItemByYear

# Create your views here.
# @login_required
def index(request):
  enrollment_list = ProjectionItemByYear.objects.filter(year__gte = 2010).order_by('id')
  semester_list = list(ProjectionItemByYear.objects.filter(year__gte = 2010).values_list('semester', flat=True).order_by('id'))
  number_list = list(ProjectionItemByYear.objects.filter(year__gte = 2010).values_list('numberOfStudents', flat=True).order_by('id'))
  context = {'enrollment_list': enrollment_list, 
             'semester_list': semester_list,
             'number_list': number_list}
  return render(request, 'index.html', context=context)


def enrollment_index(request):
  enrollment_list = ProjectionItemByYear.objects.filter(year__gte = 2010).order_by('id')
  semester_list = list(ProjectionItemByYear.objects.filter(year__gte = 2010).values_list('semester', flat=True).order_by('id'))
  number_list = list(ProjectionItemByYear.objects.filter(year__gte = 2010).values_list('numberOfStudents', flat=True).order_by('id'))
  context = {'enrollment_list': enrollment_list, 
             'semester_list': semester_list,
             'number_list': number_list}
  return render(request, 'index.html', context=context)

# def attemptedCredits_index(request):
#   attemptedCredits_list = ProjectionItemByYear.objects.filter(year__gte = 2010).order_by('id')
#   semester_list = list(ProjectionItemByYear.objects.filter(year__gte = 2010).values_list('semester', flat=True).order_by('id'))
#   number_list = list(ProjectionItemByYear.objects.filter(year__gte = 2010).values_list('attemptedCredits', flat=True).order_by('id'))
#   context = {'enrollment_list': enrollment_list, 
#              'semester_list': semester_list,
#              'number_list': number_list}
#   return render(request, 'index.html', context=context)


# def contactHours_index(request):
#   contactHours_list = ProjectionItemByYear.objects.filter(year__gte = 2010).order_by('id')
#   semester_list = list(ProjectionItemByYear.objects.filter(year__gte = 2010).values_list('semester', flat=True).order_by('id'))
#   number_list = list(ProjectionItemByYear.objects.filter(year__gte = 2010).values_list('contactHours', flat=True).order_by('id'))
#   context = {'enrollment_list': enrollment_list, 
#              'semester_list': semester_list,
#              'number_list': number_list}
#   return render(request, 'index.html', context=context)