from django.db import models

# Create your models here.

class EnrollmentItemByYear(models.Model):
  SEMESTER_CHOICES = [(1, 'Fall'), (0, 'Spring')]
  year = models.IntegerField()
  isFall = models.IntegerField(choices=SEMESTER_CHOICES)
  semester = models.CharField(max_length=20)
  numberOfStudents = models.IntegerField()
  attemptedCredits = models.IntegerField()
  contactHours = models.IntegerField()
  unemploymentRateLastYear = models.DecimalField(max_digits=6, decimal_places=4)


  def semesterFullName(self):
    s = 'Fall' if self.isFall == 1 else 'Spring'
    return str(int(self.year)) + ' ' + s
  # semesterFullName.short_description = "Full Name of Semester"
  # semester = property(semesterFullName)

# todo: pull the data from cams day by day

# class EnrollmentItemByDay(models.Model):
#   date = models.DateField(auto_now_add=True)
#   enrollment = models.IntegerField()


